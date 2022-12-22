#include <iostream>
#include <vector>
#define RED 1
#define BLUE 2

using namespace std;

//1707 - 이분 그래프

int K,V,E;

vector<vector<int>> graph;
vector<int> isVisited;

//그래프 색칠하기
void DFS(int cur){
    //아직 방문하지 않는 정점이라면 빨간색으로 칠한다.
    if(!isVisited[cur]) isVisited[cur]=RED;

    //현재 정점과 연결된 정점들을 모두 방문
    for(int i=0 ;i<graph[cur].size();i++){
        int next=graph[cur][i];

        //아직 방문하지 않은 정점이라면 현재 정점과 반대되는 색으로 칠한다.
        if(!isVisited[next]){
            if(isVisited[cur]==RED) isVisited[next]=BLUE;
            else if(isVisited[cur]==BLUE) isVisited[next]=RED;
            DFS(next); 
        }
    }
}
//이분 그래프 인지 확인하는 함수
bool isBipartite(){
    //모든 정점들을 돌아보면서 인접한 정점과의 색이 같은지 확인
    for(int cur=1;cur<=V;cur++){
        for(int i=0;i<graph[cur].size();i++){
            int next=graph[cur][i];
            //만일 인접한 정점과 색이 같다면 이분 그래프가 아님
            if(isVisited[cur]==isVisited[next])return false;
        }
    }
    return true;
}

void reset(){
    for(int i=1;i<=V;i++){
        graph[i].clear();
    }
}

int main()
{

    int vertax1,vertax2;
    cin>>K;
    
    for(int caseNum=1;caseNum<=K;caseNum++){
        cin>>V>>E;
        graph.assign(V + 1, vector<int>(0, 0));
        isVisited.assign(V + 1, false);
        
        for(int i=0;i<E;i++){
            cin>>vertax1>>vertax2;
            graph[vertax1].push_back(vertax2);
            graph[vertax2].push_back(vertax1);
        }
        for(int i=1;i<=V;i++){
            if(!isVisited[i]) DFS(i);
        }
        
        if(isBipartite())cout<<"YES\n";
        else cout<<"NO\n";
        
    }
    return 0;
}
