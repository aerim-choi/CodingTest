#include <iostream>
using namespace std;

int N; //1부터 N까지 자연수 중에서
int M; //중복 없이 M개를 고른 수열
int result[10]={0};
bool check[10]={false};

void dfs(int depth) {

	if (depth == M) {
		for (int i = 0; i < M; i++) {
			cout << result[i] << " ";
		}
		cout << "\n";

	}
	else {
		for (int i = 1; i <= N; i++) {
			if (check[i] == false) {
				result[depth] = i;
				check[i] = true;
				dfs(depth + 1);
				check[i] = false;
			}
		}
	}
}


int main() {

	cin >> N >> M;
	
	dfs(0);
	return 0;
}
