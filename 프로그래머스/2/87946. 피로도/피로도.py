from itertools import permutations

def solution(k, dungeons):
    dungeons_route = list(permutations(range(0,len(dungeons)), len(dungeons)))
    
    max_result = -1
    
    for route in dungeons_route:
        result = find_result(route,k,dungeons)
        if  result > max_result :
            max_result = result
            # print("루트 발견:",route)
        else:
            continue

    return max_result


def find_result(route,k,dungeons):
    result = 0
    for i in route:
        if dungeons[i][0] <= k:
            result += 1
            # print(dungeons[i][0],"입장",dungeons[i][1],"체력감소")
            k-= dungeons[i][1]      
        else :
            break
    
    return result