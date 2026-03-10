# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
city_num =  int(input())
costs = [list(map(int, input().split())) for _ in range(city_num)]

visited = [False] * city_num
route = []
min_cost = 999999999999999999999999999999


def dfs(cur, total):
    global min_cost

    if total>=min_cost:
        return

    if len(route) == city_num:
        if costs[cur][0] != 0:
            min_cost = min(total+costs[cur][0], min_cost)
        return
    
    for i in range(city_num):
        if not visited[i] and costs[cur][i] != 0:
            visited[i] = True   
            route.append(i)
            dfs(i, total+costs[cur][i])
            route.pop()
            visited[i] = False

visited[0] = True
route.append(0)
dfs(0,0)
print(min_cost) 



