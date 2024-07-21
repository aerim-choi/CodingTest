def solution(array):
    max_num = -1
    max_idx = -1
    for idx, element in enumerate(array):
        if max_num < element:
            max_num = element
            max_idx = idx
    answer = [max_num, max_idx]
    return answer