#include <iostream>
#include <cmath>
using namespace std;


int main() {
	int N;
	int graph[300];
	int dp[300];
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> graph[i];
	}

	dp[0] = graph[0];  
	
	dp[1] = graph[0] + graph[1]; 

	dp[2] = graph[2] + max(graph[0], graph[1]); 
	
	for (int i = 3; i < N; i++) {
		dp[i] = max(dp[i - 2] + graph[i], dp[i - 3] + graph[i - 1] + graph[i]);
	}

	cout << dp[N - 1];
}
