n,m = map(int,input().split())
init_list = list(map(int, input().split()))

max_num=0

combination=[]

def choose(curr_num_idx, cnt):
    if curr_num_idx ==n:
        if cnt==m:
            global max_num
            xor_list= list(map(int, combination))
            result = 0
            for i in xor_list:
                result = result ^ i 
            max_num = max(result,max_num)
        return 
    
    #curr_num을 뽑았을때
    combination.append(init_list[curr_num_idx])
    choose(curr_num_idx+1, cnt+1)
    combination.pop()

    #curr_num을 뽑지 않앗을 때
    choose(curr_num_idx+1,cnt)

choose(0,0)
print(max_num)