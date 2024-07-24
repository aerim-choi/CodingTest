def solution(num, k):
    num_list = list(str(num))
    k = str(k)
    if k in num_list:
        answer = num_list.index(k)+1
    else:
        answer=-1
    return answer