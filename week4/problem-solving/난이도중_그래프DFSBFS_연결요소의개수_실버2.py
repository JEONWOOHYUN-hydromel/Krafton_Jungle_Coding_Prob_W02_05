# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724
import sys
input = sys.stdin.readline

from collections import deque

num_nod, num_edge = map(int, input().split())

par = [-1] * num_nod
route = {}
for i in range(num_nod):
    route[i] = []

for _ in range(num_edge):
    nod1, nod2 = map(int, input().split())
    nod1 -= 1
    nod2 -= 1

    route[nod1].append(nod2)
    route[nod2].append(nod1)

for k in range(num_nod):
    if par[k] == -1:
        que = deque([k])
        par[k] = k

        while que:
            cur = que.popleft()
            for nxt in route[cur]:
                if par[nxt] == -1:
                    par[nxt] = k
                    que.append(nxt)

print(len(set(par)))