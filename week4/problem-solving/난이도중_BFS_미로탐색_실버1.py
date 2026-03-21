# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

vec = [[0, 1], [0, -1], [1, 0], [-1, 0]]

visited = [[False] * m for _ in range(n)]
que = deque()
que.append([0,0,1])
visited[0][0] = True
while que:
    cur = que.popleft()
    
    if cur[0] == n-1 and cur[1] == m-1:
        print(cur[2])
        break

    cnt = cur[2]+1
    for v in vec:
        new_y = cur[0]+v[0]
        new_x = cur[1]+v[1]

        if 0 <= new_y < n and 0 <= new_x < m:
            pass
        else:
            continue

        if board[new_y][new_x] == 1 and not visited[new_y][new_x]:
            que.append([new_y, new_x, cnt])
            visited[new_y][new_x] = True
        