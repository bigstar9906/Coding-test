#include <stdio.h>
#include <stdlib.h>

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
    free (arr);
    return 0;
}
