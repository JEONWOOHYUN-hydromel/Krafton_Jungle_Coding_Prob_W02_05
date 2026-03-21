# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707
import sys
from collections import deque

input = sys.stdin.readline

num_case = int(input())
for _ in range(num_case):
    num_ver, num_edge = map(int, input().split())

    route = {}
    for i in range(num_ver):
        route[i] = []

    for j in range(num_edge):
        ver1, ver2 = map(int, input().split())

        ver1-=1
        ver2-=1

        route[ver1].append(ver2)
        route[ver2].append(ver1)
    
    c = 1
    color = [-1]*num_ver
    isBipa = True
    for k in range(num_ver):
        if color[k] != -1:
            continue
                
        que = deque()
        que.append(k)
        while que:
            cur = que.popleft()

            if color[cur] == -1:
                color[cur] = c
            
            for l in route[cur]:
                if color[l] == -1:
                    color[l] = 1-color[cur]
                    que.append(l)

                elif color[l] == color[cur]:
                    isBipa = False
                    break
                                
            c = 1-c

            if not isBipa:
                break
        
    print("YES" if isBipa else "NO")