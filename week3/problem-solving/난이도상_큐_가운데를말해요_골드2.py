# 큐 - 가운데를 말해요 (백준 골드2)
# 문제 링크: https://www.acmicpc.net/problem/1655
import sys
import heapq

input = sys.stdin.readline


min_heap = []
max_heap = []

n = int(input())

for _ in range(n):
    num = int(input())
    
    if len(min_heap) >= len(max_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if min_heap and -max_heap[0] > min_heap[0]:
        a = -heapq.heappop(max_heap)
        b = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -b)
        heapq.heappush(min_heap, a)
    
    print(-max_heap[0])