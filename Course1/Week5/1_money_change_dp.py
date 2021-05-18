# Uses python3
import sys
import math

def get_change_fast(money, coins):
    coin_count = [0] * money
    for c in range(len(coin_count)):
        min_count = math.inf
        curr_money = c + 1
        for coin in coins:
            if curr_money == coin:
                curr_count = 1
            elif curr_money > coin:
                prev_money = curr_money - coin
                curr_count = coin_count[prev_money - 1] + 1
            else:
                curr_count = math.inf
            if curr_count < min_count:
                min_count = curr_count
        coin_count[c] = min_count
    
    return (coin_count[money - 1])

def get_change(money, coins):
    coin_count = 0
    if money <= 0:
        coin_count = 0
    elif money in coins:
        coin_count = 1
    else:
        coin_count = math.inf
        for coin in coins:
            if money > coin:
                money_left = money - coin
                coins_left = get_change(money=money_left, coins=coins)
                coin_count = min(coin_count, coins_left + 1)
    return coin_count

if __name__ == '__main__':
    money = int(sys.stdin.readline())
    coins = [1, 3, 4]
    print(get_change_fast(money=money, coins=coins))
