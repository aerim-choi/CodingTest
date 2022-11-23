#include <iostream>
#include <string>
using namespace std;
//시간복잡도 
//공간복잡도 : O(1)
int quadTree[64][64] = { 0 };

void recur(int n, int y, int x) {
	if (n == 1) { //원소가 1개인 경우
		cout << quadTree[y][x];
		return;
	}

	bool zero = true; //영역이 모두 0인경우
	bool one = true; //영역이 모두 1인경우

	for (int i = y; i < y + n; i++) {
		for (int j = x; j < x + n; j++) {
			if (quadTree[i][j]) { //영역에 1이 있을 경우
				zero = false; //영역이 모두 0아님 
			}
			else {//영역에 0이 있을 경우
				one = false; //영역이 모두 1 아님
			}
		}
	}

	if (zero)
		cout << 0;
	else if (one)
		cout << 1;
	else {
		cout << "(";
		recur(n / 2, y, x); //왼쪽 위
		recur(n / 2, y, x + n / 2); //오른쪽 위
		recur(n / 2, y + n / 2, x);//왼쪽 아래
		recur(n / 2, y + n / 2, x + n / 2);//오른쪽 아래
		cout << ")";
	}
	

}

int main() {
	int N;
	cin >> N;
	string line;
	
	for (int i = 0; i < N; i++) {
		cin >> line;
		for (int j = 0; j < N; j++) {
			quadTree[i][j]=line[j]-'0'; //line[j]는 문자라 0빼줘야함
		
		}
	}
	
	recur(N,0,0);

	return 0;

}
