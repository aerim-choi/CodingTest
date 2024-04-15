def solution(numbers, direction):
    answer=[]
    if direction =="right":
        answer.append(numbers.pop())
        for num in numbers:
            answer.append(num)
    
    else :
        last_num = numbers.pop(0)
        for num in numbers:
            answer.append(num)
        answer.append(last_num)    
    return answer