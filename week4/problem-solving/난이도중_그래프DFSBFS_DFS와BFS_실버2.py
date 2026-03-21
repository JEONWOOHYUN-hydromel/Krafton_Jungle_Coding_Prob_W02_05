# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
import sys
from collections import deque

input = sys.stdin.readline

num_nod, num_edge, start = map(int, input().split())
start -= 1

route = {}
for i in range(num_nod):
    route[i] = []

for j in range(num_edge):
    nod1, nod2 = map(int, input().split())

    nod1 -= 1
    nod2 -= 1
    
    route[nod1].append(nod2)
    route[nod2].append(nod1)

for i in range(num_nod):
    route[i].sort()

#dfs
visited = []
stack = [start]
while stack:
    cur = stack.pop()
    if cur in visited:
        continue
    visited.append(cur)


    for d in route[cur][::-1]:
        if d not in visited:
            stack.append(d)


print(" ".join(map(lambda x: str(x + 1), visited)))

#bfs
visited = []
que = deque()
que.append(start)
while que:
    cur = que.popleft()
    visited.append(cur)

    for b in route[cur]:
        if b not in visited and b not in que:
            que.append(b)

print(" ".join(map(lambda x: str(x + 1), visited)))