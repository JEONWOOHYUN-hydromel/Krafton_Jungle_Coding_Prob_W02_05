# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
import sys
input = sys.stdin.readline

n = int(input())

if n < 3:
    print(n)

else:
    a, b = 1, 2
    for i in range(3, n+1):
        a, b = b, (a+b)%15746
    print(b)