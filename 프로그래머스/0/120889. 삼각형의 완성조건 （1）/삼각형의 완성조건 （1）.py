def solution(sides):
    max_side_idx = sides.index(max(sides))
    max_side_length = max(sides)
    sum = 0
    
    for i in range(0,3,1):
        if i == max_side_idx :
            continue
        else:
            sum+=sides[i]
    
    
    if sum > max_side_length:
        return 1
    else:
        return 2
  