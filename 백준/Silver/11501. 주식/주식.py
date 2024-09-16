T = int(input()) #테스트케이스 수
stock_price = []
for i in range(T):
    N = int(input()) #날의 수

    stock_price_list = list(map(int, input().split()))
    max_stock_price = stock_price_list[-1]

    profit = 0

    #배열을 뒤에서 부터 최댓값을 갱신하며 푼다.
    for i in range(N):
        if max_stock_price < stock_price_list[(N-1)-i]:
           max_stock_price = stock_price_list[(N-1)-i]
        elif max_stock_price > stock_price_list[(N-1)-i] :
            profit += (max_stock_price - stock_price_list[(N-1)-i])
        else: #같으면
            continue

    print(profit)







