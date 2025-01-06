#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int a,b,c;

	scanf("%d %d", &a, &b);
	scanf("%d", &c);

	b = b + c;
	a = a + (b / 60);
	b = b % 60;

	if (a >= 24) {
		a = a % 24;
	}

	printf("%d %d\n", a, b);


	return 0;
}