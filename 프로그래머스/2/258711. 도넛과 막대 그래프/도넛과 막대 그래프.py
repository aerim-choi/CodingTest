def solution(edges):
    #정점 노드 :들어오는 간선이 없고 나가는 간선이 2개 이상이다.
    #도넛 모양 그래프, 막대모양 그래프, 8자모양 그래프의 수의합은 2이상이기 때문이다.
    #막대 그래프 : 나가는 간선이 없고, 들어오는 간선이 1개이상이다.
    #8자 그래프 : 나가는 간선 2개 드러오는 간선 2개 이상이다.
    #도넛 그래프 :  정점 노드 나가는 간선 - 막대그래프 개수 - 8자 그래프
    result = 0
    
    inout_dict= make_inout_dict(edges)
    for key,value in inout_dict.items():
        print(key,value)

def make_inout_dict(edges):
    inout_dict={}
    for edge in edges:
        node1=edge[0] #out
        node2=edge[1] #in
        
        if not node1 in inout_dict: 
            inout_dict[node1]=[0,0]
            
        if not node2 in inout_dict:
            inout_dict[node2]=[0,0]
        
        inout_dict[node1][0]+=1 #out
        inout_dict[node2][1]+=1 #in
        
    return inout_dict