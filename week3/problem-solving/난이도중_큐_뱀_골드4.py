# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
from collections import deque

num_board = int(input())

num_apple = int(input())    
apples = set()
for _ in range(num_apple):
    row, col = map(int, input().split())
    apples.add((row-1, col-1))

num_cmd = int(input())
cmds = {}
for _ in range(num_cmd):
    sec, d = input().split()
    cmds[int(sec)] = d

sec = 0
isSnake = [[False] * num_board for _ in range(num_board)]

x = 0
y = 0
prev = deque([(0, 0)])
isSnake[0][0] = True

dir_num = 0
dir_mat = [(0,1), (1,0), (0,-1), (-1,0)]   # (dy, dx)

while True:
    isApple = False

    # move
    x += dir_mat[dir_num % 4][1]
    y += dir_mat[dir_num % 4][0]

    # game end?
    if x >= num_board or x < 0 or y >= num_board or y < 0 or isSnake[y][x]:
        print(sec + 1)
        break
    
    #save
    prev.append((y, x))
    isSnake[y][x] = True

    # apple?
    if (y, x) in apples:
        apples.remove((y, x))
        isApple = True

    # tail update
    if not isApple:
        py, px = prev.popleft()
        isSnake[py][px] = False

    #next sec
    sec += 1

    #new dir
    if sec in cmds:
        d = cmds[sec]
        if d == 'D':
            dir_num += 1
        else:
            dir_num += 3