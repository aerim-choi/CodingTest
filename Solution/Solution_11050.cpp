//동적프로그래밍 문제
#include <iostream>
using namespace std;

int BC[500][500];
int main() {
	int n, r;
	cin >> n >> r;

	for (int row = 1; row <= n + 1; row++) {
		for (int col = 1; col <= r + 1; col++) {
			if (col == 1 || col == row) //1처리 최적의 원칙=>동적 프로그래밍 
				BC[row][col] = 1;
			else {
				BC[row][col] = BC[row- 1][col- 1] + BC[row - 1][col];
			}
		}
	}
	cout << BC[n+1][r+1];
	
	return 0;

}
