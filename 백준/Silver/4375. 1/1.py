def solution(n):
    temp = 1
    while(True):
        if(temp % n == 0 ):
            return len(str(temp))
        else :
            temp = temp * 10 +1
            
if __name__ == "__main__":
    while True:
        try:
            n = int(input()) 
            print(solution(n))
        except:
            break
  