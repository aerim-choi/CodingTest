//greedy algorithm
//재귀함수
#include <iostream>
#include <vector>
using namespace std;

int N, M;
int ans=0;
vector<int> card;

void blackJack(int idx, int cnt, int tmp) {
	if (cnt == 3 && tmp <= M) { //카드 3개를 더한 결과가 M이하라면 
	//현재 더한 값 vs 지금까지의 최대 값 비교 후 더큰 값을 ans저장
		ans = max(tmp, ans);
		return;
	}
	//카드를 다 탐색 했거나 카드를 3개 넘게 고르면 재귀 끝
	if (idx >= N || cnt > 3)return;
	//해당카드 선택
	blackJack(idx + 1, cnt + 1, tmp + card[idx]);
	//해당카드 선택X
	blackJack(idx + 1, cnt, tmp);
}


int main() {
	int num;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> num;
		card.push_back(num);
	}
	blackJack(0, 0, 0);
	cout << ans;
}

//for문
#include <iostream>
#include <vector>
using namespace std;
int main() {
	vector<int> card; 
	int N, M;
	cin >> N >> M;

	//카드 값 입력 및 vector초기화
	int num;
	for (int i = 0;i < N;i++) {
		cin >> num;
		card.push_back(num);
	}

	int ans = 0, tmp = 0;
	for (int i = 0;i < N - 2;i++) {
		for (int j = i + 1;j < N - 1;j++) {
			for (int k = j + 1; k < N; k++) {
				tmp = card[i] + card[j   ] + card[k];
				//M을 넘지 않으면서 현재까지 최대합(ans)보다 tmp가 크면
				if (tmp <= M && ans < tmp)ans = tmp; //ans값 갱신
			}
		}
	}
	cout << ans << "\n"; return 0;

}
