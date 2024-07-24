def solution(quiz):
    result = []
    for q in quiz:
        q = q.split('=')
        statement = q[0]
        answer=q[1]
        
        if eval(statement) == int(answer):
            result.append("O")
        else : 
            result.append("X")
        
    return result