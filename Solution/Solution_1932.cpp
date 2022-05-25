#include <iostream>
#include <algorithm>
using namespace std;

int integers[500][500]; //삼각형의 크기는 1이상 500이하이다.

int main() {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0 ; j < i + 1; j++) {
			cin >> integers[i][j];
		}
	}
	for (int i = n - 1; i >= 1; i--) {
		for (int j = 0; j < i; j++) {
			integers[i - 1][j] += max(integers[i][j], integers[i][j + 1]);
		}
	}
	cout << integers[0][0];
}
