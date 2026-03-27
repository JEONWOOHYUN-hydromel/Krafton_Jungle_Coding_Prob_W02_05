# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline

num_case = int(input())
for _ in range(num_case):
    num_coin = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0]*(target+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target+1):
            dp[i] += dp[i-coin]

    print(dp[target])