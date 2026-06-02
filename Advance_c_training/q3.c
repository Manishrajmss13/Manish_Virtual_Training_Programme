#include <stdio.h>
#include <stdlib.h>

int searchMatrix(int **mat,int rows,int cols,int key){
    int row = 0;
    int col = cols - 1;
    while(row<rows && col>=0){
        if (mat[row][col] == key) return 1;
        else if (mat[row][col] > key) col--;
        else row++;
    }
    return 0;
}

int main(){
    int rows, cols, key;
    printf("Enter number of rows and columns: ");
    scanf("%d %d", &rows, &cols);
    int **mat = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++){
        mat[i] = (int *)malloc(cols * sizeof(int));
        printf("Enter elements of row %d: ", i + 1);
        for (int j = 0; j < cols; j++) scanf("%d", &mat[i][j]);
        
    }
    printf("Enter key to search: ");
    scanf("%d", &key);
    if (searchMatrix(mat, rows, cols, key))  printf("Key found in the matrix.\n");
    else  printf("Key not found in the matrix.\n");
    

    for (int i = 0; i < rows; i++) free(mat[i]);
    free(mat);
    return 0;
}