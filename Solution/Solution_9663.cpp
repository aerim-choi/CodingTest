#include <iostream>
using namespace std;


//시간복잡도 O(N^(N+1)) //공간복잡도 O(N)
int N; //크기가 NxN인 체스판
int ans = 0; //퀸 N개를 서로 공격할 수 없도록 배치하는 경우의 수
int chess[15]; //cureentRow(현재행)에서 몇 번째 열에 퀸이 놓였는지 담는 배열 1<=N<=15

//유망성 검사
bool isPromising(int currentRow) { 
	for (int i = 0; i < currentRow; i++) { //i가 열값임
		//같은 열, 대각선상에 있는지 검사
		if (chess[i] == chess[currentRow] || currentRow - i == abs(chess[currentRow] - chess[i]))
			                                     //행의차    ==           //열의차
			return false;
	}
	return true;
}
void nqueen(int currentRow) {
	//basecase: 마지막 행까지 수행하면 종료
	if (currentRow == N) {
		ans += 1;
		return;
	}
	//현재 검사할 행의 모든 열에 퀸을 하나씩 놓아보며 공격가능성 검사
	for (int col = 0; col < N; col++) {
		chess[currentRow] = col;

		//유망하면 currentRow까지 확정지은 상태를 가지고 다음 행 검사
		if (isPromising(currentRow))
			nqueen(currentRow + 1);
	}
}

int main() {
	cin >> N;
	nqueen(0);
	cout << ans << endl;
	return 0;
}
