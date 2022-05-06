//스택사용
//시간복잡도 O(N) / 공간복잡도O(N)
#include <iostream>
#include <stack>
using namespace std;

int main() {
	int  N;
	cin >> N;
	int* arr = new int[N];
	int* ans = new int[N];
	stack<int> s;

	for (int i = 0;i < N;i++) {
		cin >> arr[i];
	}


	for (int i = N - 1;i >= 0;i--) {
		while (!s.empty() && s.top() <= arr[i]) {
			s.pop();
		}
		if (s.empty())ans[i] = -1;
		else ans[i] = s.top();

		s.push(arr[i]);
		
	}

	for (int i = 0;i < N;i++) {
		cout << ans[i] << " ";
	}

	return 0;
}
