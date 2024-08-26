def solution(my_string):
    
    result = 0
    num = ''
    for ch in my_string:
        if ch.isdigit():
            num+=ch
            
        else : 
            if num=='':
                continue
            else:
                result+=int(num)
                num=''
                
                
    if num.isdigit():
        result+=int(num)
            
    return result