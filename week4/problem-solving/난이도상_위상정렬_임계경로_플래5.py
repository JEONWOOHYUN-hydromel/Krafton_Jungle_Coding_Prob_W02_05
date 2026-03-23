# 위상정렬 - 임계경로 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1948
import sys
input = sys.stdin.readline

from collections import deque

num_city = int(input())
num_rode = int(input())

indegree = {}
route = {}  # key: 도시 인덱스, 0: 도착점[]
route_reversed = {}
for i in range(num_city+1):
    route[i] = []
    route_reversed[i] = []
    indegree[i] = 0

for _ in range(num_rode):
    start, end, cost = map(int, input().split())
    route[start].append((end,cost))
    route_reversed[end].append((start,cost))
    indegree[end] += 1

onestep, rome = map(int, input().split())

dist = [-1] * (num_city+1)
dist[onestep] = 0
que = deque()
que.append(onestep)
while que:
    cur  = que.popleft()
    
    for nxt, cost in route[cur]:
        dist[nxt] = max(dist[nxt], dist[cur] + cost)
        
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            que.append(nxt)

count = 0
que.append(rome)
visited = [False]*(num_city+1)
while que:
    cur = que.popleft()
    for prev, cost in route_reversed[cur]:
        if dist[cur]-cost == dist[prev]:
            count += 1

            if not visited[prev]:
                visited[prev] = True
                que.append(prev)

print(dist[rome])
print(count)