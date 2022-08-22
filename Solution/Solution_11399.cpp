#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//시간복잡도O(nlogn)/공간복잡도O(N)

int main()
{
    int N;
    int temp;
    vector<int> waitTime;
    cin >> N;
    
    for(int i=0; i < N; i++){
        cin >> temp;
        waitTime.push_back(temp);
    }
   
    //오름차순정렬
    sort(waitTime.begin(), waitTime.end());
    
   // 1+(1+2)+(1+2+3)+(1+2+3+3)+(1+2+3+3+4)
    int waitSum=0;
    int waitTemp=0;
    for(int i=0;i<waitTime.size();i++){
        waitTemp+=waitTime[i]; //1=0+1 3=1+2 6=3+3 9=6+3 13=9+4
        waitSum+=waitTemp; //1+3+6+9+13
        
    }    
    
    cout<<waitSum;
}
