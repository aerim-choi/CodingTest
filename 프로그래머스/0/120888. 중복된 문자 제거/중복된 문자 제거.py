def solution(my_string):
    list=[]
    list2 = []
    answer=''
    for ch in my_string:
        list.append(ch)
    
    for i in list:
        if i in list2:
            continue
        else:
            list2.append(i)
            
    for i in list2:
        answer+=i
        
    return answer