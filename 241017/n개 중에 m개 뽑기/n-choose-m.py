#1부터 N이하의 숫자 중 M개의 숫자를 골라 만들 수 있는 모든 조합 구하기

N,M = map(int,input().split())
answer = []

def choose(curr_num,i):
    if curr_num>M:
        for i in answer:
            print(i, end=" ")
        print()
        return

    for k in range(i,N+1):
        answer.append(k)
        choose(curr_num+1,k+1)
        answer.pop()

choose(1,1)