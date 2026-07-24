//il linguaggio c è un linguaggio compilato: cioé si ha bisogno di un compilatore che traduce il testo e determina un eseguibile
//il linguaggio python è uno interpretato: si ha bisogno di un interprete nella fase di esecuzione
//in python si fa una traduzione passo passo dall'interprete: non c'é una traduzione finale
//su linux c'è gia il gcc
//elenco di cartelle: dir sul powershell, ls su linux invece
//cd serve per cambiare directory su linux
//ls -a mi fa vedere i file nascosti
//mkdir crea una directory
//touch nome_file crea un file nella directory
//mv prende come parametri il file presente nel filesystem e la destinazione, cambiandogli volendolo
//il nome
//ls . cartella corrente
//ls ..cartella padre
//rm sta per remove

//nel momento in cui vado a compilare un programma il compliatore cerca una funzione chiamata main. La funzione main viene eseguita nel momento in cui il programmma viene lanciato
//se vogliamo stampare qualcosa abbiamo bisogno di una libreria
//si mette il tipo di varibaile per via delle specifiche del linguaggio: ci si riferisce a uno spazio di memoria

float my_abs(float a){
    if (a<0){
    return -a;
    }

    else{
    return a;
    }
}

//sto ritornando un float


int main()
{
//qui c'é il blocco della funzione con le parentesi graffe
    printf("Hello world!\n"); //si va a capo con \n

    float x=20; //dihiarazione ed inizializzazione di variabile (che è un pezzo di memoria fisso, non come in python che l'oggetto si aggiorna)
    //si può scrivere semplicemente anche solo float x;
    float g; //dichiarazione
    g=5; //inizializzazione
    //in c le variabili corrispondono a pezzi di memoria che contengono dei dati
    while (my_abs(g*g-x)>0.00001){
        g=(g+x/g)/2;
    }

    printf("La radice quadrata di %f = calcolata: %f\n", x,g); //la funzione printf come parametri di input prende sempre una stringa
    //printf stampa un float contenuto in g al posto di "%f"
    //si usa %d per gli interi

}
