#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    
    unordered_map<string,int> um; 
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());
   
    for(int i=0;i<phone_book.size();i++){
        int str_len=phone_book[i].length();
        
        um[phone_book[i].substr(0,str_len)]++;
        
        if(i+1<phone_book.size()){
            cout<<phone_book[i+1].substr(0,str_len)<<endl;
            um[phone_book[i+1].substr(0,str_len)]++;
            if(um[phone_book[i].substr(0,str_len)]>1){
                answer=false;
                //return false;
            }
            um[phone_book[i+1].substr(0,str_len)]=0;
        }
        
        um[phone_book[i].substr(0,str_len)]=0;
        
    }
    
    return answer;
}
