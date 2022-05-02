#include<stdio.h>
#include<math.h>
int main()
{
    float e,f;
    int a,b,c,d,i;
    char n[20];
    printf("Enter Amount Given\n");
    scanf("%d",&a);
    printf("Enter year in which loan given\n");
    scanf("%d",&b);
    printf("Choose corresponding serial no. for your loan type \n 1 zero interest \n 2 simple interest \n 3 compound interest\n");
    scanf("%d",&c);
    switch(c)
    {
        case 1:
        printf("Loan is given at zero interest \n write name of benificiery\n");
        scanf("%s",&n);
        d=0;
        e=a;
        printf("Name is %s \n Interest percentage is %d \nloan tenure is %d\n Amount to return %.2lf \n",n,d,2021-b,a);
        break;
        case 2:
        printf("Loan is given at simple interest \n write name of benificiery\n");
        scanf("%s",&n);
        printf("write interest per annum\n");
        scanf("%d",&d);
        f=2021-b;
        e=a+(a*d*f)/100;
        printf("Name is %s \n Interest percentage is %d \nloan tenure is %.2lf\n Amount to return %.2lf \n",n,d,f,e);
        break;
        case 3:
        printf("Loan is given at compound interest \n write name of benificiery\n");
        scanf("%s",&n);
        printf("write interest per annum\n");
        scanf("%d",&d);
        f=2021-b;
        e=a*(pow((1+d/100),f));
        printf("Name is %s \n Interest percentage is %d \nloan tenure is %.2lf\n Amount to return %.2lf \n",n,d,f,e+a);
        break;
    }
    return 0;
}
