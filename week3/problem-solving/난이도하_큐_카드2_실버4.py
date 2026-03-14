# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque

n = int(input())
arr = [i for i in range(1, n+1)]
que = deque(arr)

num = -1
isOdd = True
while que:
    num = que.popleft()
    if isOdd:
        isOdd = False
    else:
        que.append(num)
        isOdd = True
print(num)