#include <iostream>
#include <algorithm>
#include<vector>
using namespace std;


bool visited[100001] = { false };
int N, M, R;
int cnt = 0;
int result[100001];
void dfs(vector<vector<int>> adj, int r) { //정점집합 v, 간선집합 e, 시작정점 r

	if (visited[r] == true) {
		return;
	}



	else {  //visited == false
		visited[r] = true;//시작정점 R 방문했다고 표시
		
		result[r] = cnt++;

		sort(adj.begin(), adj.end());
		for (int i = 1; i <= adj.size(); i++) { //정점R의 인접 정접 집함( 정접 번호를 오름 차순으로 방문한다.
			dfs(adj, i);
			
		}


	}


}

//int main() {
//	// 정점의 수 N (5 ≤ N ≤ 100,000)
//	//간선의 수 M (1 ≤ M ≤ 200,000)
//	//시작 정점 R (1 ≤ R ≤ N)
//
//	int vertax1, vertax2;
//	cin >> N >> M >> R;
//	int** adjMatrix = new int* [N + 1];
//
//	for (int i = 0; i < N + 1; i++) {
//		adjMatrix[i] = new int[N + 1];
//
//	}
//
//	for (int i = 0; i < N + 1; i++) {
//		for (int j = 0; j < N + 1; j++) {
//			adjMatrix[i][j] = 0;
//		}
//
//	}
//	
//	for (int i = 0; i < M; i++) {
//		cin >> vertax1 >> vertax2;
//		//양방향 그래프
//		adjMatrix[vertax1][vertax2] = 1;
//		adjMatrix[vertax2][vertax1] = 1;
//	}
//
//	dfs(adjMatrix, 1);
//	sort(result, result + N);
//	for (int i = 1; i <= N; i++) {
//		cout << result[i] << endl;
//	}
//	// 동적 할당 해제
//	for (int i = 0; i < N + 1; i++) //N개의 행
//		delete[] adjMatrix[i]; // 한 행을 가리키는 포인터
//	delete[] adjMatrix; // 배열 전체를 가리키는 포인터
//
//	return 0;
//}

int main() {
	// 정점의 수 N (5 ≤ N ≤ 100,000)
	//간선의 수 M (1 ≤ M ≤ 200,000)
	//시작 정점 R (1 ≤ R ≤ N)

	int vertax1, vertax2;
	cin >> N >> M >> R;
	vector<vector<int>> adj(N,vector<int>(N,0));

	for (int i = 0; i < M; i++) {
		cin >> vertax1 >> vertax2;
		//양방향 그래프
		adj[vertax1].push_back(vertax2);
		adj[vertax2].push_back(vertax1);
	}

	dfs(adj,1);
	sort(result, result + N);
	for (int i = 1; i <= N; i++) {
		cout << result[i] << endl;
	}
	
	return 0;
}
