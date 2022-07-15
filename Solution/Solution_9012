#include <iostream>
#include <string>
#include <stack>

using namespace std;

/*checkVPS 함수 
시간복잡도 O(N) :for문 한개
공간복잡도 O(N) : stack 1개 */
bool checkVPS(string str) {
    stack<char> st;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '(')st.push('('); //'(' 인경우 스택에 push
        else { //) 인경우 
            if (st.empty()) { //스택이 비었을 경우: 오른쪽 괄호가 더 많은 문자열
                return false;
            }
            else { //')'인경우 pop하여 괄호 짝 맞추기
                st.pop();
            }
        }
    }
    //왼쪽 괄호가 스택에 남아있을 경우: 왼쪽 괄호가 더 많은 문자열
    return st.empty() ? true : false;
}

int main() {
    int T;
    string str;

    cin >> T;

    for (int i = 0; i < T; i++) {
        cin >> str;
        if (checkVPS(str))cout << "YES" << endl;
        else cout << "NO" << endl;
    }

    return 0;
}
