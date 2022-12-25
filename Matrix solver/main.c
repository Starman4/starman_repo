//This program solves Ax=b
//A is a diagonal matrix
//b is an array


#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>




//Function for greeting user and entring the program
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


//Function for solution to Ax=b
int equation_solver(int in_sel){

    int nrow,ncol,nb,i,j,ctrl1=0;

    //Taking dimensions from user
    printf("Please enter how many rows you want for your matrix A : \n");
    scanf("%d",&nrow);
    printf("Please enter how many columns you want for your matrix A: \n");
    scanf("%d",&ncol);
    printf("Enter the dimension of b: \n");
    scanf("%d",&nb);
    printf("\n");

    float b_array[nrow];
    float mat[nrow][nrow];

    //Checking if the dimensions are appropriate
    if(nb==nrow){
        if(in_sel==1){

            printf("Please enter your matrix:\n\n");

            //Row and column inputs
            for(i=1;i<=nrow;i++){
                for(j=1;j<=ncol;j++){
                    printf("Enter the [%d][%d] element of your matrix: \n",i,j);
                    scanf("%f",&mat[i-1][j-1]);
                }
                printf("Next row\n");
                printf("\n");
            }


            //Testing for diagonality
            int ctrl2=0,ctrl3=0;

            for(int k=0;k<nrow;k++){
                for(int l=0;l<ncol;l++){
                    if(k!=l && mat[k][l]!=0){
                        ctrl2=1;
                        break;
                    }}}

            for(int k=0;k<nrow;k++){
                for (int l = 0; l < ncol; l++){
                    if (k == l && mat[k][l] == 0){
                        ctrl3 = 1;
                        break;
                    }}}


            //Diagonality test result
            if(ctrl2==1 || ctrl3==1){
                printf("Your matrix is not a diagonal Matrix.\n");
                printf("Please enter an appropriate matrix!\n");}


            else if(ctrl2==0 && ctrl3==0){
                printf("Your Matrix is a diagonal Matrix.\n");
                printf("\n");
                ctrl1=1;}


            //Requesting array b after test result
            if(ctrl1==1){


                printf("Here is matrix A that you entered:\n");
                for (int k = 0; k < nrow; k++) {
                    for (j = 0; j < ncol; j++) {
                        printf("%.4f \t", mat[k][j]);
                    }
                    printf("\n");}

                printf("\n");

                for (int l=0; l<nrow; ++l ) {
                    printf("Please enter your solution array b[%d]: \n",l+1);
                    scanf("%f", &b_array[l]);}
                printf("\n\n");





                //Taking inverse of matrix A
                float in_mat[nrow][ncol];
                float val;

                for (int k = 0; k <nrow ; k++){
                    val=mat[k][k];
                    val=1/val;
                    in_mat[k][k]=val;}
                printf("\n");


                //Finding the solution array
                float sol_array[nrow];
                float val1,val2;

                for (int k = 0; k <nrow ; k++){
                    val1=in_mat[k][k];
                    val2=b_array[k];
                    sol_array[k]=val1*val2;
                }

                //Printing the matrix A
                printf("Here is your matrix A: \n");
                printf("\n");
                for (int k = 0; k <nrow ; k++){
                    for (int l = 0; l <ncol ; l++) {
                        printf("%.4f \t", mat[k][l]);
                    }
                    printf("\n");}

                //Printing the array b
                printf("Here is your array b:\n\n");
                for(int j = 0; j <nrow ; ++j) {
                    printf("%.4f\n", b_array[j]);}

                //Printing the solution array
                printf("Here is your solution array :\n\n");
                for(int j = 0; j <nrow ; j++) {
                    printf("%.4f\n", sol_array[j]);}
                printf("\n\n\n");
            }

            //If the result is negative requesting inputs again
            if(ctrl1==0){

                equation_solver(in_sel);}}

        //Assigning random variables according to user sellection
        else if(in_sel==2){
            srand(time(NULL));
            for(int o = 0; o<nrow; o++)
                for(int p = 0; p<ncol; p++)
                    mat[o][p] = rand()%100+1;

            for(int o = 0; o<nrow; o++)
                for(int p = 0; p<ncol; p++)
                    if(o!=p)
                        mat[o][p] =0;

            for (int k = 0; k < nrow; k++) {
                for (j = 0; j < ncol; j++) {
                    printf("%.4f \t", mat[k][j]);
                }
                printf("\n");}

            for (int k = 0; k < nrow; k++){
                b_array[k]=rand()%100+1;}

            for (int k = 0; k < nb; k++) {
                printf("%.4f",b_array[k]);

            }
            //Taking inverse of matrix A
            float in_mat[nrow][ncol];
            float val;

            for (int k = 0; k <nrow ; k++){
                val=mat[k][k];
                val=1/val;
                in_mat[k][k]=val;}
            printf("\n");

            //Finding the solution array
            float sol_array[nrow];
            float val1,val2;

            for (int k = 0; k <nrow ; k++){
                val1=in_mat[k][k];
                val2=b_array[k];
                sol_array[k]=val1*val2;
            }


            //Printing the matrix A
            printf("Here is your matrix A: \n");
            for (int k = 0; k <nrow ; k++){
                for (int l = 0; l <ncol ; l++) {
                    printf("%.4f \t", mat[k][l]);
                }
                printf("\n");}

            //Printing the araay b
            printf("Here is your array b: \n");
            for (int k = 0; k < nb; k++){
                printf("%.4f \n",b_array[k]);}

            //Printing the solution array
            printf("Here is your solution array :\n\n");
            for(int j = 0; j <nrow ; j++) {
                printf("%.4f\n", sol_array[j]);}
            printf("\n\n\n");

        }
        }

    //if the dimensions are not appropriate asking for entering again
    else if(nb!=nrow){
        printf("Dimension of your array b is not appropriate.\n");
        printf("Please enter a valid dimension!\n\n");
        equation_solver(in_sel);}
    }


int main(){

    //variable declerations
    int a,in_sel;
    int b=true;

    //Taking users selection

    while(b){
        a=user_selection();

        if(a==1){
            printf("Equation solver selected!\n\n");
            printf("Press '1' for manual input\n");
            printf("Press '2' for random assignment\n\n");
            printf("Please Enter an input method:");
            scanf("%d",&in_sel);
            printf("\n");
            equation_solver(in_sel);
            continue;
        }
        else if(a==2){
            printf("Exiting!!!");
            b=false;}

    return 0;
}}


//Sait Metin Yurdakul	040210111
//Arda Boran Özcan	    040200103
//Furkan Akbaba	        040200391
