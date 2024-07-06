def solution(n):
    
    answer = []
    d=2
    while n != 1:
        if n % d != 0:
            d += 1
        else:
            n //= d
            answer.append(d)
            
    answer = list(set(answer))
    answer.sort()
    return answer