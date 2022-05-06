//방법1 : 인접행렬로 구현
#include <iostream>
using namespace std;

#define MAX_SIZE 501 //친구수 최대 500명인데 친구학번이 500까지가능하니 501로 잡는다.

int main() {

	//상근이의 동기의 수
	int n;
	//리스트의 길이
	int m;

	bool matrix[MAX_SIZE][MAX_SIZE] = { false }; //상근이 친구관계 
	bool friendArr[MAX_SIZE] = { false }; //상근이 결혼식 초대할 친구

	int relation1;
	int relation2;

	cin >> n;
	if (n < 2 || n > 500)
		return 0;
	
	cin >> m;
	if (m < 1 || m > 10000)
		return 0;
	 
	
	for (int i = 0; i < m; i++) {
		cin >> relation1 >> relation2;
		matrix[relation1][relation2] = true;
		matrix[relation2][relation1] = true;
	}
	
	for (int i = 2; i <= n; i++) {
		if (matrix[1][i]) {
			friendArr[i] = true; //상근이 친구
			for (int j = 2; j <= n; j++) {
				if (matrix[i][j])
					friendArr[j] = true; //상근이 친구의 친구
			}
		}
	}

	int count = 0;
	for (int i = 2; i <= n; i++) {
		if (friendArr[i])count++;
	}
	cout << count;
	return 0;
}
//방법2 : 인접리스트로 구현
#include <iostream>
#include <vector>
using namespace std;

#define MAX_SIZE 501 //친구수 최대 500명인데 친구학번이 500까지가능하니 501로 잡는다.

int main() {

	//상근이의 동기의 수
	int n;
	//리스트의 길이
	int m;

	int relation1;
	int relation2;
	vector<int> w[MAX_SIZE]; //상근이의 친구 관계
	bool friendArr[MAX_SIZE] = { false }; //상근이 결혼식 초대할 친구

	cin >> n;
	if (n < 2 || n > 500)
		return 0;

	cin >> m;
	if (m < 1 || m > 10000)
		return 0;

	
	for (int i = 0; i < m; i++) {
		cin >> relation1 >> relation2;
		w[relation1].push_back(relation2);
		w[relation2].push_back(relation1);
	}


	for (int v : w[1]) {
		friendArr[v] = true;	//상근이의 친구
			for (int k : w[v])
					friendArr[k] = true; //상근이의 친구의 친구			

	}

	int count = 0;
	for (int i = 2; i <= n; i++) {
		if (friendArr[i]) {
			count++;
		}
	}
	cout << count;

	return 0;
}
