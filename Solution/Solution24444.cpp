#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int N, M, R;
int visitNum = 0;
int visited[100001] = { 0, };
deque<int> graph[100001];

void bfs(int r) {
	deque<int> temp;
	if (visited[r]> 0) {
		return;
	}
	visited[r] = ++visitNum; //시작 정점 R을 방문 했다고 표시한다.
	temp.push_back(r); //큐 맨 뒤에 시작 정점 R을 추가한다.

	while (!temp.empty()) {
		int u= temp.front(); 
		temp.pop_front();   //큐 맨 앞쪽의 요소(u)를 삭제한다.
		for (int v = 0; v < graph[u].size(); v++) {
			if (visited[graph[u][v]] == 0) {
				visited[graph[u][v]] =++visitNum; //u 인접 정점을 방문했다고 표시한다.
				temp.push_back(graph[u][v]);	 //u 인접 정점을 큐 맨 뒤에 추가한다.
			}
		}
	}

}



int main() {


	cin >> N >> M >> R;

	int vertax1;
	int vertax2;
	for (int i = 0; i < M; i++) {
		cin >> vertax1 >> vertax2;
		graph[vertax1].push_back(vertax2);
		graph[vertax2].push_back(vertax1);
	}

	for (int i = 0; i < N + 1; i++) { //오름차순 정렬
		sort(graph[i].begin(), graph[i].end());

	}

	bfs(R);
	
	for (int i = 1; i < N + 1; i++) {
		cout << visited[i] << '\n';
	}


	return 0;
}
