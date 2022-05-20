//backtracking, dynamic programming
#include <iostream>
#include <vector>
using namespace std;

int N; //수열의 항의 개수
int temp;
vector<int> A; //수열
int op[4] = { 0,0,0,0 }; //연산자의 개수
int mymax = -100000001;
int mymin = 100000001;

void getAnswer(int result, int idx) {
	if (idx == N) { //인덱스 == 항의개수
		if (result > mymax)mymax = result;
		if (result < mymin)mymin = result;
		return;
	}
	for (int i = 0; i < 4; i++) {
		if (op[i] > 0) {
			op[i]--; //연산자 하나 사용했으므로 1개 줄어듬 
			if (i == 0)
				getAnswer(result + A[idx], idx + 1);
			else if (i == 1)
				getAnswer(result - A[idx], idx + 1);
			else if (i == 2)
				getAnswer(result * A[idx], idx + 1);
			else 
				getAnswer(result / A[idx], idx + 1);
		
			op[i]++; //다른 연산자를 사용할 것이므로 아까 줄였던 연산자 개수 늘려줌
		}
	}
	return;
}

int main() {

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> temp;
		A.push_back(temp);
	}

	for (int i = 0; i < 4; i++) {
		cin >> temp;
		op[i] = temp;
	}
	getAnswer(A[0], 1);
	cout << mymax << endl;
	cout << mymin;

	return 0;
}
