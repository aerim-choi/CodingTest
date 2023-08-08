
#1
import math
def solution(num1, num2):
    answer = (num1/num2)*1000
    return math.trunc(answer)
#2
def solution(num1, num2):
    return 1 if num1==num2 else -1
#3
import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer=numer1*denom2+numer2*denom1
    denom=denom1*denom2
    
    gcd=math.gcd(numer,denom)
    
    answer.append(numer//gcd)
    answer.append(denom//gcd)
    
    return answer
#4
def solution(numbers):
    answer = list(map(lambda x: x*2,numbers))
    return answer
