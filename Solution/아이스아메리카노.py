# def solution(money):
#     answer = []
    
#     cup= money//5500
#     change = money - 5500 * cup
#     answer.append(cup)
#     answer.append(change)
    
#     return answer

def solution(money):

    answer = [money // 5500, money % 5500]
    return answer
