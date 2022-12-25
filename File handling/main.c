#include <stdio.h>
#include <string.h>
#include <conio.h>
char ch;

struct stock_status{
    char name[15];
    int stock;
    float price;
};


int main(){


    struct stock_status i1;
    struct stock_status i2;
    struct stock_status i3;


    strcpy(i1.name,"apple");
    strcpy(i2.name,"tomato");
    strcpy(i3.name,"pear");

    i1.stock=24;
    i1.price=4.65;

    i2.stock=45;
    i2.price=2.12;

    i3.stock=12;
    i3.price=3.26;


    int length=strlen(i1.name);
    int length2=strlen(i2.name);
    int length3=strlen(i3.name);

    FILE *Fptr;

    Fptr=fopen("Stock status.txt","w");



    for(int i=0; i<length;++i){
        fputc(i1.name[i],Fptr);}
    fprintf(Fptr,"\t %d \t %.2f\n",i1.stock,i1.price);

    for(int i=0; i<length2;++i){
        fputc(i2.name[i],Fptr);}
    fprintf(Fptr,"\t %d \t %.2f\n",i2.stock,i2.price);

    for(int i=0; i<length3;++i){
        fputc(i3.name[i],Fptr);}
    fprintf(Fptr,"\t %d \t %.2f\n",i3.stock,i3.price);

    fclose(Fptr);
    getch();

    Fptr=fopen("Stock status.txt","r");
    while(!feof(Fptr)){
        ch=fgetc(Fptr);
        printf("%c",ch);
    }


    fclose(Fptr);
    getch();
    return 0;
}
