#include <iostream>
#include <vector>
using namespace std;

int main() {

	int T; //테스트 케이스의 수
	int N; //국가의 수 : vertax
	int M; //비행기의 종류  : edge 

	vector<int> adj[1001];
	int vertax1;
	int vertax2;

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin>> N >> M;
		for (int j = 0; j < M; j++) {
			cin >> vertax1 >> vertax2;
			adj[vertax1].push_back(vertax2);
			adj[vertax2].push_back(vertax1);
		}
		cout << N - 1<<endl;
		
		for (int i = 1; i <= N; i++) {
			adj[i].clear();
		}
	}

	return 0;
}
