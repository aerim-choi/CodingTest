def solution(hp):
    #장군개미 5 , 병정개미 3, 일개미 1
    
    result = hp // 5 # 4 = 23 // 5
    hp = hp % 5 #  hp = 23 % 5 = 3
    
    result += hp // 3 # 5 = 4 + 1
    hp = hp % 3 # 3 % 3 = 0
    
    result += hp // 1 # 5=5 + 0
    hp = hp % 1 
        
    return result