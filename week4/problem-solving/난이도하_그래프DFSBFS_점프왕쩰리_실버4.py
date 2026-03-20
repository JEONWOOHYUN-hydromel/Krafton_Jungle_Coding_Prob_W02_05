# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

que = deque()
que.append([0, 0])
while que:
    cur = que.popleft()
    val = board[cur[0]][cur[1]]
    if val == 0:
        pass
    elif val == -1:
        print("HaruHaru")
        sys.exit()

    else:
        next0 = cur[0]+val
        next1 = cur[1]+val

        if next0 < n:
            que.append([next0, cur[1]])
        
        if next1 < n:
            que.append([cur[0], next1])
    
print("Hing")