#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) 
{
	int a, b;
	int c;
	scanf("%d", &c);
	for (int i = 0; i < c; i++)
	{
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n",i+1,a+b);

		
	}
	return 0;
}
