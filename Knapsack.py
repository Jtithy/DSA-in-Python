# Author: Tithy
# Date: 2026-02-19
# Description: Knapsack Algorithm Implementation in Python

def knapsack(W, wt, val, n):
    K = [[0 for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
                
                
    return K[n][W]


val = [10, 30, 100, 120, 150]
wt = [20, 50, 70, 90, 110]
W = 50
n = len(val)

print("Max value: ", knapsack(W, wt, val, n))

                