# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(10**6)
pre = list(map(int, sys.stdin.read().split()))

def post(start, end):
    #base case
    if start >= end:
        return
    
    #where to cut
    root = pre[start]
    mid = end
    for i in range(start+1, end):
        if root < pre[i]:
            mid = i
            break

    #left
    post(start+1, mid)

    #right
    post(mid, end)

    #root
    print(root)

post(0, len(pre))