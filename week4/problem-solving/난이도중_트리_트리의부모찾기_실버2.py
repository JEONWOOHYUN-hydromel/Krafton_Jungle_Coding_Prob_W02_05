# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

num_nod = int(input())
edges = {}
for i in range(1, num_nod+1):
    edges[i] = []

for _ in range(num_nod-1):
    nod1, nod2 = map(int, input().split())
    edges[nod1].append(nod2)
    edges[nod2].append(nod1)

par = {1:0}

def dfs(nod):    
    for nxt in edges[nod]:
        if nxt not in par:
                par[nxt] = nod
                dfs(nxt)

dfs(1)
for j in range(2, num_nod+1):
    print(par[j])
