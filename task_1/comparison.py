def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1] 
    coin_count = {} 
    for coin in coins:
        if amount >= coin:
            count = amount // coin  
            coin_count[coin] = count  
            amount -= count * coin

    return coin_count


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 
    coin_used = [0] * (amount + 1)
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin 

    coin_count = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1
        amount -= coin

    return coin_count


amount = 113

greedy_result = find_coins_greedy(amount)
print("Greedy Result:", greedy_result)

min_coins_result = find_min_coins(amount)
print("Min Coins Result:", min_coins_result)
