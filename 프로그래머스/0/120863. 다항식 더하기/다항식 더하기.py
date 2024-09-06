def solution(polynomial):
    
    expression = polynomial.split(' + ')
    
    x_sum = 0 #1차식 합계
    c_sum = 0 #상수항 합계
    
    for e in expression:
        
        if e =='x':
            x_sum+=1
        
        elif e[-1] == 'x':
            e = e.replace('x','')
            x_sum+=int(e)
            
        else:
            c_sum+=int(e)
    
    result = ''
    if x_sum > 0 and c_sum > 0:
        if x_sum==1:
            result = 'x'+' + '+ str(c_sum)
        else:
            result = str(x_sum) + 'x' + ' + '+ str(c_sum)
    elif x_sum > 0 and c_sum ==0 :
        if x_sum==1:
            result = 'x'
        else:
            result = str(x_sum) +'x'
    elif x_sum ==0 and c_sum >0:
        result = str(c_sum)
    
    return result