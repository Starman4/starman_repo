#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>
#include <dvec.h>



int user_selection(){
    int user_self,ctrl;

    printf("Welcome to equation solver!\n\n");
    printf("Enter '1' for equation solver\n");
    printf("Enter '2' for exiting the program\n\n");
    printf("Please enter your selection: ");


    if(scanf("%d",&user_self)){
        ctrl=true;
        while(ctrl){
            if(user_self==1){
                return 1;
            }
            else if(user_self==2){
                return 2;
            }
            else{
                printf("please enter a valid integer!");
                return user_selection();
            }
        }}
    else{
        printf("please enter an integer");
        return user_selection();
    }}



int equation_solver(int in_sel){

    double mat[25][25];
    int nrow,ncol,i,j,ctrl1=0;
    int ctrl;


    if(in_sel==1){
        //row ve column sayısını alma
        printf("enter how many rows you want:\n");
        scanf("%d",&nrow);
        printf("enter how many columns you want:\n");
        scanf("%d",&ncol);
        printf("enter the matrix:\n\n");

        //row ve column inputları
        for(i=1;i<=nrow;i++){
            for(j=1;j<=ncol;j++){
                printf("Enter the [%d][%d] element of your matrix:",i,j);
                scanf("%f",&mat[i][j]);
            }
            printf("Next row\n");
            printf("\n");
        }


        //diagonallık testi
        int ctrl2=0,ctrl3=0;

        for(int k=1;k<nrow;k++){
            for(int l=0;l<ncol;l++){
                if(k!=l && mat[k][l]!=0){
                    ctrl2=1;
                    break;
                }}}

        for(int k=1;k<nrow;k++){
            for (int l = 0; l < ncol; l++){
                if (k == l && mat[k][l] == 0){
                    ctrl3 = 1;
                    break;
                }}}


        //diagonallık testi sonuç
        if(ctrl2==1 || ctrl3==1)
            printf("Given Matrix is not a diagonal Matrix.\n");


        else if(ctrl2==0 && ctrl3==0){
            printf("Given Matrix is a diagonal Matrix.");
            ctrl1=1;}


        //test sonucuna göre b arrayi istemi
        if(ctrl1==1){
            float b_array[nrow];

            printf("Here is your matrix:\n\n");
            for (int k = 1; k <= nrow; k++) {
                for (j = 1; j <= ncol; j++) {
                    printf("%.2f \t", mat[k][j]);
                }
                printf("\n");}

            for (int l=0; l<nrow; ++l ) {
                printf("Please enter your solution array b:");
                scanf("%f", &b_array[l]);}



            printf("Here is your array b:\n\n");
            for(int j = 0; j <nrow ; j++) {
                printf("%.2f\n", b_array[j]);}

            //taking inverse
            float in_mat[nrow][ncol];
            float val;

            for (int k = 1; k <=nrow ; k++){
                val=mat[k][k];
                val=1/val;
                in_mat[k][k]=val;}
            printf("\n");
            for (int k = 1; k <=nrow ; k++){
                for (int l = 1; l <=ncol ; l++) {
                    printf("%.2f \t", in_mat[k][l]);
                }
                printf("\n");

            }

            //finding the solution array
            float sol_array[nrow];
            float val1,val2;

            for (int k = 1; k <=nrow ; k++){
                val1=in_mat[k][k];
                val2=b_array[k-1];
                sol_array[k-1]=val1*val2;
            }


            //printing the soluntion array

            printf("Here is your solution array :\n\n");
            for(int j = 0; j <nrow ; j++) {
                printf("%.2f\n", sol_array[j]);}

        }

        //test sonucuna göre tekrar input istemi

        if(ctrl1==0){
            equation_solver(in_sel);}}

    else if(in_sel==2){
        printf("random");
        printf("enter how many rows you want:\n");
        scanf("%d",&nrow);
        printf("enter how many columns you want:\n");
        scanf("%d",&ncol);

        int p, o;

        srand(time(NULL));
        for(o = 0; o<=nrow; o++)
            for(p = 0; p<=ncol; p++)
                mat[o][p] = rand();
        for (int k = 1; k <= nrow; k++) {
            for (j = 1; j <= ncol; j++) {
                printf("%.2f \t", mat[k][j]);
            }
            printf("\n");}}

}










int main(){

    int a,in_sel;

    a=user_selection();

    if(a==1){
        printf("Equation solver selected!\n\n");
        printf("Please Enter an input method:\n");
        printf("Press '1' for manual input\n");
        printf("Press '2' for random assignment\n");
        scanf("%d",&in_sel);
        equation_solver(in_sel);
    }
    else if(a==2){
        printf("exiting!");}
    return 0;
}