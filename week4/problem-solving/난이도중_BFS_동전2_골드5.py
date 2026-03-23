# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

#DP 반복문
import sys
input = sys.stdin.readline

num_coin, target = map(int, input().split())
coins = sorted(set(int(input()) for _ in range(num_coin))) 

INF = 10001
dp = [INF]*(target+1)
dp[0] = 0

for coin in coins:  #작은 코인부터 
    for i in range(coin, target+1): #끝까지 일단 만들고
        dp[i] = min(dp[i], dp[i-coin]+1)    #이후 코인에서 괜찮으면 업데이트

print(dp[target] if dp[target] != INF else -1)

#재귀 + 메모이제이션
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

num_coin, target = map(int, input().split())
coins = sorted(set(int(input()) for _ in range(num_coin)))

memo = {}
INF = 10001

def min_coin(x):
    if x == 0:
        return 0
    if x < 0:
        return INF
    if x in memo:
        return memo[x]

    #없으면 확실한 min으로 저장
    ans = INF
    for coin in coins:
        if coin > x:    #이후 코인은 더 크니까 break
            break
        ans = min(ans, min_coin(x - coin) + 1)

    memo[x] = ans
    return ans

result = min_coin(target)
print(result if result != INF else -1)