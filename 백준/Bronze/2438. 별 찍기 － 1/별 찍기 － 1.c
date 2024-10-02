#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)

{
	
	int n;
	int i=0;
	int j = 0;
	scanf("%d", &n);

	while (i<n)
	{
		j = 1;
		i++;
		while (j<=i) 
		{
			printf("*");
			j++;
			
		}
		printf("\n");

	}

	return 0;

}