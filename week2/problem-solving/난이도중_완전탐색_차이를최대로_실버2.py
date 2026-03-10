# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819
n = int(input())
arr = list(map(int, input().split()))

visited = [False] * n
picked = []
max_result = 0

def cal_arr(arr):
    total = 0
    for i in range(len(arr)-1):
        total += abs(arr[i]-arr[i+1])
    return total

def dfs():
    global max_result

    if len(picked) == n:
        max_result = max(max_result, cal_arr(picked))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            picked.append(arr[i])
            dfs()
            picked.pop()
            visited[i] = False
    
dfs()
print(max_result)
