def solution(cap, n, deliveries, pickups):
    deliveries_stack = make_stack(deliveries)
    pickups_stack= make_stack(pickups)
    
    print(deliveries_stack)
    print(pickups_stack)
    answer = -1
    return answer

def make_stack(list):
    stack=[]
    idx = 1 
    for i in list:
        for j in range(0,i,1):
            if not i:
                stack.add(idx)
            else : 
                pass
    return stack

