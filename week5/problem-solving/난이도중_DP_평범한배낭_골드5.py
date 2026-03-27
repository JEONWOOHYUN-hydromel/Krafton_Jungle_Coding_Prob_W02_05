# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst_item = list(tuple(map(int, input().split())) for _ in range(n))
dp = [0] * (k+1)

for w, v in lst_item:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[k])