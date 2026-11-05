from typing import Callable
from random import randint
from collections import Counter
from spn import SBOX, SBOX_INV, PERM, NR, key_from_hex, sub, permute, encrypt
from params import BLOCK_L, BLOCK_M, SBOX_NO, GROUP_MASK, SIZEOF_INT, MSG_NO, MSG_MASK

def new_key():
    ukey = input("Chiave (20 cifre esadecimali): ") or "{:0>20X}".format(randint(0, 0xFFFFFFFFFFFFFFFFFFFF))
    return key_from_hex(ukey)

FORMAT16B = "{:0>16b}"

SBOX_FN = lambda x: SBOX[x]
SBOX_INV_FN = lambda x: SBOX_INV[x]

def mask_inv(mask: int) -> int:
    return ~mask & MSG_MASK

def sbox_delta_pairs(delta: int):
    """Generate all possible bit group pairs with
    difference delta having the same size of an sbox"""
    currmsg = 0
    while currmsg < SBOX_NO:
        yield currmsg, currmsg ^ delta
        currmsg += 1

def sbox_probable_dout(sbox: list[int]) -> list[int]:
    """Return a list of bit groups.  
    Given the sbox any two inputs with difference i, output[i]
    contains the most probable difference of the two outputs."""
    # set all elements of a list to 0
    def reset_list(l: list[int]):
        for i in range(len(l)): l[i] = 0

    # at index i most probable output delta of an
    # sbox given two inputs with difference i
    # index 0 has deterministic output 0
    probable_dout = [0] * SBOX_NO
    # distribution of output deltas of an sbox
    # given two inputs with difference din
    din_distrib = [0] * SBOX_NO

    for din in range(1, SBOX_NO):
        reset_list(din_distrib)
        for x1, x2 in sbox_delta_pairs(din):
            dout = sbox[x1] ^ sbox[x2]
            din_distrib[dout] += 1
        probable_dout[din] = max( enumerate(din_distrib), key=lambda x: x[1] )[0]

    return probable_dout

def probable_diff_at_round(din: int, sbox: list[int], perm: list[int], rounds: int):
    """Calculate the most probable difference that
    two inputs will have after _rounds_ rounds of SPN.  
    _din_ is the difference of the two inputs."""
    common_d = sbox_probable_dout(sbox)
    # follow the difference through the SPN
    # ignore key sums as they are linear operations
    for _ in range(rounds):
        din = sub(din, common_d)
        din = permute(din, perm)
    return din

def zeroed_groups_mask(x: int) -> int:
    """Return a mask having 1 where bit groups are all 0."""
    mask = 0
    group_mask = GROUP_MASK
    for _ in range(BLOCK_M):
        if x & group_mask == 0: mask |= group_mask
        group_mask <<= BLOCK_L
    return mask

def is_right_pair(y1: int, y2: int, zero_mask: int) -> bool:
    return ((y1 ^ y2) & zero_mask) == 0

def candidate_keys(mask: int):
    """Generate all possible candidate keys, zeroed where mask = 1."""
    k = mask
    while k <= MSG_MASK:
        yield k & mask_inv(mask)
        k += 1
        k |= mask

def backtrack(y: int, sbox_inv: list[int], key: int):
    r"""Take an encrypted message _y_ through
    a key and the inverse _sbox\_inv_ of an sbox."""
    y = y ^ key
    return sub(y, sbox_inv)

type encryptcb = Callable[[int], int]

def diffattack(delta: int, tries: int, encrypt: encryptcb, is_delta_in: bool = True ) -> tuple[list[tuple[int, int]], int]:
    r"""Tries a differential attack agains _encrypt_ with _tries_ pairs
    of plaintexts having difference _delta_ if _is\_delta\_in_ is True.  
    If _is\_delta\_in_ is False, uses delta as the difference
    to use in the attack.  
    Returns the most probable key alongside a mask set to 1 on valid probable key bits."""

    if is_delta_in:
        delta = probable_diff_at_round(delta, SBOX, PERM, NR-1)
    # delta = 0x1100
    # per il punto c dell'esercizio, questo delta ci darebbe 4 bit, 
    # invece per darne 8 dobbiamo metterlo uguale a 1100 
    # boom parametrizzato ez
    mask = zeroed_groups_mask(delta)
    candidates: Counter = Counter()
    
    for _ in range(tries):
        x1 = randint(0, MSG_MASK)
        x2 = x1 ^ delta
        y1 = encrypt(x1)
        y2 = encrypt(x2)
        if not is_right_pair(y1, y2, mask): continue
        for k in candidate_keys(mask):
            y1u = backtrack(y1, SBOX_INV, k)
            y2u = backtrack(y2, SBOX_INV, k)
            if ((y1u ^ y2u) & mask_inv(mask)) != delta: continue
            candidates[k] += 1

    return candidates.most_common(5), (mask_inv(mask) if len(candidates) > 0 else 0)

def apply_mask(guess: int, mask: int) -> str:
    guess_mask = ( ((guess>>i)&1, (mask>>i)&1) for i in range(SIZEOF_INT-1, -1, -1) )
    return ''.join( '_' if m==0 else '1' if g else '0' for g, m in guess_mask )

def print_da(delta: int, tries: int, encrypt: Callable[[int, list[int]], int] = encrypt,
             keysched: list[int]|None = None, is_delta_in: bool = True) -> None:
    if keysched is None:
        keysched = new_key()
    guesses = diffattack(delta, tries, lambda x: encrypt(x, keysched), is_delta_in)
    to_guess = keysched[-1]
    guess_mask = guesses[1]
    print("key:", FORMAT16B.format(to_guess), sep='\t')
    for g in guesses[0]:
        print("guess:", apply_mask(g[0], guess_mask), '←' if g[0] == to_guess & guess_mask else '', sep='\t')

if __name__ == '__main__':
    delta = int(input(f"Differenza in ingresso (4 cifre hex, default = 0x9009): ") or '0x9009', 16)
    is_delta_in: bool = not (input(f"Utilizzare {delta:0>#6X} direttamente per l'attacco? (y/n, default = n): ").strip('\n ') in ('Y', 'y'))
    tries = int(input("Numero di known plaintext (default = 1000): ") or '1000')
    print_da(delta, tries, is_delta_in=is_delta_in)

# anche qui bisogna cambiare la differenza in ingresso da 0B00 che c'era a 0x9009