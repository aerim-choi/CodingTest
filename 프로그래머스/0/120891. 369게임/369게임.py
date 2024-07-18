def solution(order):
    order = str(order)
    clap = 0
    for i in order:
        if i=='3' or i=='6' or i=='9':
            clap+=1   
    
    return clap