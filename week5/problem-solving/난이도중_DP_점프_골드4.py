# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253
import sys
input = sys.stdin.readline

INF = 10001

num_stone, num_small = map(int, input().split())
small = set(int(input()) for _ in range(num_small))

limit = int((2 * num_stone) ** 0.5) + 2

dp = [{} for _ in range(num_stone + 1)]
dp[1][0] = 0
for i in range(1, num_stone+1):
    for v in range(1, limit+1):
        
        if i-v < 1:
            break

        #small stone -> no update
        if i in small:
            continue
        
        best = min(
            dp[i-v].get(v-1, INF), 
            dp[i-v].get(v, INF), 
            dp[i-v].get(v+1, INF)
        )

        if best != INF:
            dp[i][v] = best+1


#도착 확인
result = min(dp[num_stone].values(), default=INF)
print(result if result != INF else -1)