# replace()사용
def solution(my_string, letter):
    return my_string.replace(letter, '')
  
#나의 풀이
def solution(my_string, letter):
    new_string=''
    for ch in my_string:
        if(ch!=letter):
            new_string+=ch
    return new_string
