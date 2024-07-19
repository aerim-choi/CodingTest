def solution(numbers):
    number = ''
    answer = ''
    for ch in numbers:
        number += ch
        if number =='zero':
            answer +='0'
            number =''
        elif number == 'one':
            answer +='1'
            number =''
        elif number == 'two':
            answer +='2'
            number =''
        elif number == 'three':
            answer +='3'
            number =''
        elif number == 'four':
            answer +='4'
            number =''
        elif number == 'five':
            answer +='5'
            number =''
        elif number == 'six':
            answer +='6'
            number =''
        elif number == 'seven':
            answer +='7'
            number =''
        elif number == 'eight':
            answer +='8'
            number =''
        elif number == 'nine':
            answer +='9'
            number =''
        else:
            continue
    return int(answer)