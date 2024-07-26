def solution(my_string):
    my_string_list = []
    for i in my_string:
        my_string_list.append(i.lower())
        
    my_string_list = sorted(my_string_list)
    
    return "".join(my_string_list)