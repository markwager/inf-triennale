x=20 #è fisso (variabile=simbolo associato ad un valore)
g=5 #varia (variabile) ("=" operatore asimmetrico e serve per assegnare un valore al simbolo)

while abs(g*g-x)>0.00001 : #ripeti fintanto che g^2 non si avvicina a x
    g=(g+x/g)/2
print(g) #funzione incorporata
#ciclo+condizione+contenuto
#abs è una funzione incorporata
#esistono numeri interi e float
#possiamo confrontare numeri con abs e normali tra loro sulla console per ottenere un valore logico bool
#si possono separare le parti su spyder con "# In["ci puoi scrivere random"]"

# In[]
#new version
#inizializzazione delle variabili
x=20 #è fisso (variabile=simbolo associato ad un valore)
g=150
while abs(g-x/g)>0.00001 : #ripeti fintanto che g^2 non si avvicina a x
    print(type(g))
    g=(g+x/g)/2
print(g)
#se fai 4/2 rimane float perchè non è 2 ma 2.0
#il float vince sempre sull'int

# In[]
x=input() #(il type dell'input è di tipo str cioè è una stringa sempre)
x=int(x) #conversione da stringa ad intero, oppure usi float(x) perchè potrebbe insorgere l'errore di "ValueError"
g=150
while abs(g-x/g)>0.00001 : #ripeti fintanto che g^2 non si avvicina a x
    print(type(g))
    g=(g+x/g)/2
print(g)

