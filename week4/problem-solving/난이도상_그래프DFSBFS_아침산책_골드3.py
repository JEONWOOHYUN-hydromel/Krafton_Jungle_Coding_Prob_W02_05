# 그래프, DFS, BFS - 아침 산책 (백준 골드3)
# 문제 링크: https://www.acmicpc.net/problem/21606
import sys
input = sys.stdin.readline

from collections import deque

num_nod = int(input())
isIn = list(input().strip())

route = {}
for i in range(num_nod):
    route[i] = []

count = 0
for _ in range(num_nod-1):
    n1, n2 = map(int, input().split())
    n1 -= 1
    n2 -= 1
    route[n1].append(n2)
    route[n2].append(n1)

    #야외를 안거치는 경우 count
    if isIn[n1] == '1' and isIn[n2] == '1':
        count += 2


#야외를 거치는 경우
#야외 섬을 찾아서 섬에 연결된 실내 수 n구하고, count += n*(n-1) 

#전 노드 순회 ()
visited = [False]*(num_nod)
for j in range(num_nod):
    if isIn[j] == '1' or visited[j]:
        continue
    
    #신대륙
    que = deque()
    que.append(j)
    visited[j] = True
    num_indoor = 0
    while que:
        cur = que.popleft()
        for nxt in route[cur]:
            if isIn[nxt] == '1':
                num_indoor += 1
            elif not visited[nxt]:
                que.append(nxt)
                visited[nxt] = True

    count += num_indoor*(num_indoor-1)

print(count)