def solution(s):
    word_dict = {}
    for ch in s:
        if ch in word_dict:
            word_dict[ch]+=1
        else:
            word_dict[ch]=1
    
    answer_list= []
    answer = ''
    for key, value in word_dict.items():
        if value == 1:
            answer_list.append(key)
        else:
            continue
    
    answer_list.sort()

    return answer.join(answer_list)