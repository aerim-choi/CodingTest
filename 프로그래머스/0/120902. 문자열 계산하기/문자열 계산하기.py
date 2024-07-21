def solution(my_string):
    my_string_list = my_string.split()
    sum = 0
    op = '+' #초기에는 '+' 맨 앞 숫자는 더해야함
    for idx, ch in enumerate(my_string_list):
        if ch=='+':
            op = '+'
        elif ch =='-':
            op = '-'
        else : 
            if op=='+':
                sum+=int(ch)
            else : 
                sum-=int(ch)
            
    return sum