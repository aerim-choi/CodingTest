#include <iostream>
#include <string>

using namespace std;

class Queue {
private:
	int queue[2000000];
	int f = 0, b = -1;
public:
	//push X : 정수 X를 큐에 넣는 연산이다.
	void push(int x) {
		queue[++b] = x;
	}
	//pop : 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
	//만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	void pop() {
		if (b < f ) {
			cout << -1<< '\n';
		}
		else {
			cout << queue[f++] << '\n';
		}
		
	}

	//size: 큐에 들어있는 정수의 개수를 출력한다.
	void size() {
		cout << b - f + 1<< '\n';
	}
	//empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
	void empty() {
		if (b < f ) {
			cout << 1 << '\n';
		}
		else {
			cout << 0 << '\n';
		}
	}
	//front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	void front() {
		if (b < f)
			cout << -1 << '\n';
		else {
			cout << queue[f] << '\n';
		}
	}
	//back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
	void back() {
		if (b < f )
			cout << -1 << '\n';
		else {
			cout << queue[b] << '\n';
		}
	}

};

int main() {

	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
	string cmd;

	Queue que;
	
	for (int i = 0; i < N; i++) {
		cin >> cmd;
		if (cmd == "push") {
			int x;
			cin >> x;
			que.push(x);
		}else if (cmd == "pop") {
			que.pop();
		}
		else if (cmd == "size") {
			que.size();
		}
		else if (cmd == "empty") {
			que.empty();
		}
		else if (cmd == "front") {
			que.front();
		}
		else { //cmd=="back"
			que.back();

		}
	}

	return 0;


}
