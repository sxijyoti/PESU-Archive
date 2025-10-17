#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define KEYSIZE 16

int main() {
    int i, j;
    FILE *f;
    unsigned char key[KEYSIZE];
    int value1 = 1523986729;  
    int value2 = 1523999329;

    f = fopen("keys.txt", "w");
    for (j = value1; j <= value2; j++) {
        srand(j);
        for (i = 0; i < KEYSIZE; i++) {
            key[i] = rand() % 256;
            fprintf(f, "%.2x", key[i]);
        }
        fprintf(f, "\n");
    }
    fclose(f);
    return 0;
}

