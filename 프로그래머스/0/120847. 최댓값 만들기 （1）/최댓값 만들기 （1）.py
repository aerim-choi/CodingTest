def solution(numbers):
    
    max1 = find_max(numbers)
    numbers.remove(max1)
    max2 = find_max(numbers)
    numbers.remove(max2)
    
    answer = max1 * max2
    return answer

def find_max(numbers):
    max = -1
    for i in numbers:
        if max < i :
            max = i
    return max
    