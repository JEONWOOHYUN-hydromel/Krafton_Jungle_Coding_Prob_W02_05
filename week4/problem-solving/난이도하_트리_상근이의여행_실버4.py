# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num_con, num_pln = map(int, input().split())
    
    #국가 등록
    route = {}
    for i in range(1, num_con+1):
        route[i] = []

    #하늘길 업데이트
    for _ in range(num_pln):
        con1, con2 = map(int,input().split())
        route[con1].append(con2)
        route[con2].append(con1)
    
    #경로 적은 곳 찾기
    min_pln = 0
    for j in range(1, num_con+1):
        if len(route[j]) > min_pln:
            min_con = j
            min_pln = len(route[j])
    
    #min_con부터 시작...BFS
    que = deque()
    que.append(min_con)
    visited = []
    used_pln = []
    while len(visited) < num_con:
        cur_nod = que.popleft()
        visited.append(cur_nod)
        for c in route[cur_nod]:
            if c not in visited and c not in que:
                used_pln.append([cur_nod, c])
                que.append(c)

    print(len(used_pln))