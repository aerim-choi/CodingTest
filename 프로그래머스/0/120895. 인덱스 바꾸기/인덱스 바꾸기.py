def solution(my_string, num1, num2):
    answer=''
    my_string_list = list(my_string)
    
    my_string_list[num1],my_string_list[num2] = my_string_list[num2], my_string_list[num1]
    
    return answer.join(my_string_list)