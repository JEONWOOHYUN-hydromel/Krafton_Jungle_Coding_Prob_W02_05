# 백트래킹 - 비숍 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1799
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[x == 0 for x in row] for row in arr]
cross_up = [False]*(2*n-1)
cross_down = [False]*(2*n-1)
max_num = 0
def dfs(count, idx):
    global max_num
    placed = False
    for idx in range(idx, n*n):
        i = idx // n
        j = idx % n
        c_up = i+j
        c_down = i-j+n-1
        if not visited[i][j] and not cross_up[c_up] and not cross_down[c_down]:
            visited[i][j] = True
            cross_up[c_up] = True
            cross_down[c_down] = True
            placed = True
            dfs(count+1, idx+1)
            visited[i][j] = False
            cross_up[c_up] = False
            cross_down[c_down] = False
    if not placed:
        max_num = max(max_num, count)
        
dfs(0, 0)
print(max_num)