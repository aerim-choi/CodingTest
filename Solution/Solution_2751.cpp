#include <iostream>
#define MAX_SIZE 1000000
using namespace std;

int sorted[MAX_SIZE];
void merge(int list[], int left, int mid, int right) {
	int i, j, k, l;
	i = left;
	j = mid + 1;
	k = left;

	while (i <= mid && j <= right) {
		if (list[i] <= list[j])
			sorted[k++] = list[i++];
		else {
			sorted[k++] = list[j++];
		}
	}
	if (i > mid) {
		for (l = j;l <= right;l++) {
			sorted[k++] = list[l];
		}
	}
	else {
		for (l = i;l <= mid;l++) {
			sorted[k++] = list[l];
		}
	}
	for (l = left;l <= right;l++) {
		list[l] = sorted[l];
	}
}

void merge_sort(int list[], int left, int right) {
	int mid;
	if (left < right) {
		mid = (left + right) / 2;

		//분할
		merge_sort(list, left, mid);
		merge_sort(list, mid + 1, right);
		//병합하며 정렬
		merge(list, left, mid, right);
	}
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int n;
	int array[MAX_SIZE];
	
	cin >> n;
	
	for (int i = 0; i < n;i++) {
		cin >> array[i];
	}
	merge_sort(array, 0, n - 1);
	for (int i = 0;i < n; i++) {
		cout << array[i] << '\n';
	}

	return 0;
}
