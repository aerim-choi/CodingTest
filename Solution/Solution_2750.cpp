#include <iostream>
#define MAX_SIZE 1000
using namespace std;

void quick_sort(int* data, int start, int end) {
	if (start >= end) {
		return;
	}
	int pivot = start;
	int low = pivot + 1;
	int high = end;
	int temp;

	while (low <= high) {
		while (low <= end && data[low] <= data[pivot])
			low++;
		while (high > start && data[high] >= data[pivot])
			high--;
		if (low > high) {
			temp = data[high];
			data[high] = data[pivot];
			data[pivot] = temp;
		}
		else {
			temp = data[low];
			data[low] = data[high];
			data[high] = temp;
		}

	}
	//왼쪽 부분리스트를 퀵정렬
	quick_sort(data, start, high - 1);
	//오른쪽 부분리스트를 퀵정렬
	quick_sort(data, high + 1, end);
}

int main() {
	int n;
	int array[MAX_SIZE];
	cin >> n;
	
	for (int i = 0; i < n;i++) {
		cin >> array[i];
	}
	quick_sort(array, 0, n-1);
	for (int i = 0; i < n; i++) {
		cout << array[i] << endl;
	}
	return 0;

}
