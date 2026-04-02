# DP - 외판원 순회 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/2098
import sys
input = sys.stdin.readline

INF = 10**14

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(1<<n)]

def dfs(visited, cur):
    #완료!
    if visited == (1<<n)-1:
        if cost[cur][0] == 0:
            return INF
        return cost[cur][0]
    
    #메모에 있나
    if dp[visited][cur] != -1:
        return dp[visited][cur]
    
    #없네..업데이트!
    best = INF
    for nxt in range(n):
        if visited & (1<<nxt) or cost[cur][nxt] == 0:
            continue
        
        cost_nxt = cost[cur][nxt] + dfs(visited | (1<<nxt), nxt)
        best = min(best, cost_nxt)
    
    dp[visited][cur] = best
    return best

print(dfs(1<<0, 0))
