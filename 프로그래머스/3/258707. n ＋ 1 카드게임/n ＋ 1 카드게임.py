from collections import deque
def solution(coin, cards):
    target = len(cards) + 1
    my_card = cards[:len(cards)//3]
    cards = deque(cards[len(cards)//3:])
    temp_card = []
    stage = 0

    while True:
        if len(cards) >= 2:
            temp_card.append(cards.popleft())
            temp_card.append(cards.popleft())
        stage += 1
        continue_flag = 0
        #1
        for i in my_card:
            if target - i in my_card:
                my_card.remove(i)
                my_card.remove(target - i)
                continue_flag = 1
                break
        #2
        if continue_flag == 0 and coin > 0:
            for i in temp_card:
                if target - i in my_card:
                    temp_card.remove(i)
                    my_card.remove(target - i)
                    continue_flag = 1
                    coin -= 1
                    break
        #3
        if continue_flag == 0 and coin > 1:
            for i in temp_card:
                if target - i in temp_card:
                    temp_card.remove(i)
                    temp_card.remove(target - i)
                    continue_flag = 1
                    coin -= 2
                    break

        if continue_flag:
            continue
        break

    if stage > (target-1)//3+1:
        stage = (target-1)//3+1
    return stage