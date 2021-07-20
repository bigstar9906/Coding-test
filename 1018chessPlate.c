#include <stdio.h>
#include <stdlib.h>

int compArr(char [],int,int);
int main(void)
{
    int n,m;
    scanf("%d %d",&n,&m);
    if((n<8)|(n>50)) return 0;
    if((m<8)|(m>50)) return 0;
    char temp;
    char* arr;
    arr = (char*)malloc(sizeof(char)*(n*m));
    for(int i = 0; i<(n*m);i++)
    {
        scanf("%c",&temp);
        if(temp == '\n') scanf("%c",&temp);
        if(!((temp == 'B')|(temp =='W'))) return 0 ;
        arr[i] = temp;
    }
    
    compArr(arr,n,m);
    // print arr 함수
    /*for(int i = 0;i<n;i++)
    {
        for(int j = 0;j<m;j++)
        {
            printf("%c",arr[8*i+j]);
        }
        printf("\n");
    }
    */
    printf("\n종료하려면 아무 키나 누르세요.");
    scanf("%c",&temp);
    scanf("%c",arr[0]);
    free(arr);
    return 0;
}


// 원 배열의 정해진 부분과 완벽한 체스판 arr2 를 비교하여 몇개가 다른지 리턴해 주는 함수. 원 배열의 모든 부분에 반복하여 적용하면 최소값을 찾을 수 있다. 
int compArr(char x[],int n, int m)
{
	char arr1[64];
	char arr2[64] = {'W','B','W','B','W','B','W','B','B','W','B','W','B','W','B','W','W','B','W','B','W','B','W','B','B','W','B','W','B','W','B','W','W','B','W','B','W','B','W','B','B','W','B','W','B','W','B','W','W','B','W','B','W','B','W','B','B','W','B','W','B','W','B','W'};
	for(int i = 0;i<n;i++)
    {
        for(int j = 0;j<m;j++)
        {
            arr1[8*i+j]=x[8*i+j];
        }
    }
    printf("*********************\n");
    for(int i = 0;i<n;i++)
    {
        for(int j = 0;j<m;j++)
        {
            printf("%c",arr1[8*i+j]);
        }
        printf("\n");
    }
    printf("*********************\n");
    printf("\n\n*********************\n");
    for(int i = 0;i<n;i++)
    {
        for(int j = 0;j<m;j++)
        {
            printf("%c",arr2[8*i+j]);
        }
        printf("\n");
    }
    printf("*********************\n");
    return 0;
}
