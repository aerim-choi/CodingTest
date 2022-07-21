#include <iostream>
#include <queue>
using namespace std;

queue<int> que;

int main() {
	int N, K;

	//N명의 사람 , K번째 사람 제거
	cin >> N >> K;
	
	//queue에 N명의 사람 push
	for (int i = 1; i <= N; i++) {
		que.push(i);
	}
	
	cout << "<" ;
	while (que.size()>=2) {
		for (int i = 1; i < K; i++) {
			que.push(que.front());
			que.pop();
		}
		cout  << que.front() << ", ";
		que.pop();
	}
	cout << que.front() << ">";
	que.pop();
	return 0;
}
