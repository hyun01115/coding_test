#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int a,b;

	scanf("%d %d", &a, &b);

	if (b-45<0 && a!=0) {
		printf("%d %d\n", a-1, b+15);
	}
	else if (b - 45 < 0) {
		if (a == 0) {
			a = 23;
			printf("%d %d\n", a, b + 15);
		}
	}
	else if (b-45>=0) {
		printf("%d %d\n", a, b-45);
	}


	return 0;
}