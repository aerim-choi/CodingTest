#include <iostream>
using namespace std;

bool visited[100000] = { false };
int N, M, R;
void dfs(int** adj, int r) { //정점집합 v, 간선집합 e, 시작정점 r
	
	if (visited[r] == true) {
		return;
	}

	

	else { //visited[r] ==false;
		/*for (int i = 1; i <= N; i++) {
			if (adj[r][i] == 1) {
				break;
			}
			else {
				cout << "0";
				return;
			}
		}*/
		visited[r] = true;//시작정점 R 방문했다고 표시
		cout << r << endl;
		
		
		for (int i = 1; i <= N; i++){
			for (int j = 1; j <= N; j++) {
				if (adj[r][j] == 1) {
					adj[r][j] = 0;

					cout << "dfs실행:" << j << endl;
					dfs(adj, j);
				}

			}
			
		}
		
		
	}
	

}

int main() {
	// 정점의 수 N (5 ≤ N ≤ 100,000)
	//간선의 수 M (1 ≤ M ≤ 200,000)
	//시작 정점 R (1 ≤ R ≤ N)
	
	int vertax1, vertax2;
	cin >> N >> M >> R;
	int** adjMatrix = new int* [N+1];

	for (int i = 0; i < N+1; i++) {
		adjMatrix[i] = new int[N+1];
	
	}

	for (int i = 0; i < N+1; i++) {
		for (int j = 0; j < N+1; j++) {
			adjMatrix[i][j] = 0;
		}
		
	}
	
	
	for (int i = 0; i < M; i++) {
		cin >> vertax1 >> vertax2;
		//양방향 그래프
		adjMatrix[vertax1][vertax2] = 1;
		adjMatrix[vertax2][vertax1] = 1;
	}

	dfs(adjMatrix, 1);
	for (int i = 1; i <= N; i++) {
		if (visited[i] == false) {
			dfs(adjMatrix, i);
		}
	}
	
	// 동적 할당 해제
	for (int i = 0; i < N+1; i++) //N개의 행
		delete[] adjMatrix[i]; // 한 행을 가리키는 포인터
	delete[] adjMatrix; // 배열 전체를 가리키는 포인터

	return 0;
}
