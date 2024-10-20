def main():
    n = int(input())

    stairs = [0]*301

    for i in range(1,n+1):
        stairs[i]=int(input())

    dp =[0]*301
    dp[1]=stairs[1]
    dp[2]=stairs[1] + stairs[2] #바로 올라가는 것보다 2개 밟는게 더 높음
    for i in range(3,n+1):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

    return dp[n]

print(main())