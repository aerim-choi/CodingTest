def solution(emergency):
    answer =[]
    
    for e in emergency:
        answer.append(0)
    i=1
    for e in emergency:
        max_index=emergency.index(max(emergency))
        emergency[max_index]=-1
        answer[max_index]=i
        i=i+1
    return answer