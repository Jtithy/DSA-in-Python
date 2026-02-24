# Author: Tithy
# Date: 2026-02-19
# Description: Coin Change Problem Implementation in Python

import sys

def coin_change(coins, V):
    dp = [sys.maxsize] * (V + 1)
    dp[0] = 0

    for i in range(1, V + 1):
        for coin in coins:
            if coin <= i:
                sub = dp[i - coin]
                if sub != sys.maxsize:
                    dp[i] = min(dp[i], sub + 1)

    if dp[V] == sys.maxsize:
        return -1
    return dp[V]


coins = [1, 2, 5]
V = 11

print("Minimum coins required:", coin_change(coins, V))