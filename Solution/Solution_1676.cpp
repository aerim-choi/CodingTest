#include <iostream>
#include <algorithm>

using namespace std;

//시간복잡도: O(N*M) N은 바깥 for문 , M은 temp의 5의 지수값이다.
//공간복잡도: O(1)

int main() {

	int N;
	int temp;
	int cnt = 0;
	cin >> N;
	
	for (int i = 1; i <= N; i++) {
		temp = i;
		
		while (temp % 5 == 0) {
			cnt++;
			temp /= 5;
		}
	}
	cout << cnt;
	return 0;
}
