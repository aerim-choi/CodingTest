#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> numbers) {
    
    if (numbers.size()==2){
        return numbers[0]*numbers[1];
    }
    if (numbers.size()==3){
        int max1 = *max_element(numbers.begin(), numbers.end());
        numbers.erase(max_element(numbers.begin(), numbers.end()));

        int max2 = *max_element(numbers.begin(), numbers.end());
        numbers.erase(max_element(numbers.begin(), numbers.end()));
        return max1 * max2;
    }
    
    int max1 = *max_element(numbers.begin(), numbers.end());
    numbers.erase(max_element(numbers.begin(), numbers.end()));
    
    int max2 = *max_element(numbers.begin(), numbers.end());
    numbers.erase(max_element(numbers.begin(), numbers.end()));
    
    int min1= *min_element(numbers.begin(), numbers.end()); 
    numbers.erase(min_element(numbers.begin(), numbers.end()));
    
    int min2= *min_element(numbers.begin(), numbers.end()); 
    numbers.erase(min_element(numbers.begin(), numbers.end()));
        
    int answer1 = max1*max2;
    int answer2 = min1*min2;
    
    if (answer1>=answer2){
        return answer1;
    }
    else{
        return answer2;
    }
}