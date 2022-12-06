#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;


int N, M, R;
int visitNum = 0;
int visited[100001];
vector<int> graph[100001];
void dfs(int r) {
	if (visited[r] > 0) {
		return;
	}
	visited[r] = ++visitNum; //시작 정점 r을 방문했다고 표시한다.
	for (int i = 0; i < graph[r].size(); i++) {
		dfs(graph[r][i]);
	}


}

int main() {
	// 정점의 수 N (5 ≤ N ≤ 100,000)
	//간선의 수 M (1 ≤ M ≤ 200,000)
	//시작 정점 R (1 ≤ R ≤ N)
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int vertax1, vertax2;
	cin >> N >> M >> R;


	for (int i = 0; i < M; i++) {
		cin >> vertax1 >> vertax2;
		//양방향 그래프
		graph[vertax1].push_back(vertax2);
		graph[vertax2].push_back(vertax1);
	}


	for (int i = 0; i < N + 1; i++) {
		sort(graph[i].begin(), graph[i].end());

	}
	dfs(R);
	for (int i = 1; i < N + 1; i++) {

		cout << visited[i] << '\n';
	}

	return 0;
}
