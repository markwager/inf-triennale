BLOCK_L = 4
"""s-box and group size"""

BLOCK_M = 4
"""Number of groups"""

SBOX_NO = 1 << BLOCK_L
GROUP_MASK = SBOX_NO - 1

SIZEOF_INT = BLOCK_L * BLOCK_M
MSG_NO = 1 << SIZEOF_INT
MSG_MASK = MSG_NO - 1
