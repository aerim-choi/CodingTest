def solution(numbers, target):
    answer = 0
    answer = dfs(0,0,numbers,target)
    return answer

def dfs(index, curr_sum, numbers, target): 
    #1. 탈출조건:현재 재귀함수가 call된 인덱스가 numbers.length만큼되면
    if index == len(numbers) :
        if target == curr_sum:
            return 1
        else:
            return 0
    #2. 수행동작
    else:
        answer = 0
        answer += dfs(index+1,curr_sum + numbers[index],numbers,target)#더한거
        answer += dfs(index+1,curr_sum - numbers[index],numbers,target)#뺀거
        return answer

     