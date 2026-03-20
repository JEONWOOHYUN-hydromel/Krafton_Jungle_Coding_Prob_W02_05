# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline

from collections import deque

num_com = int(input())
num_route = int(input())

route = {}
for i in range(1, num_com+1):
    route[i] = []

for _ in range(num_route):
    com1, com2 = map(int, input().split())
    route[com1].append(com2)
    route[com2].append(com1)

que = deque()
que.append(1)
virused = []
while que:
    new_com = que.popleft()
    virused.append(new_com)

    for c in route[new_com]:
        if c not in que and c not in virused:
            que.append(c)

print(len(virused)-1)