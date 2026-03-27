# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

n = int(input())
meets = [list(map(int, input().split())) for _ in range(n)]
meets.sort(key= lambda x: (x[1], x[0]))

cnt = 0
prev_end = 0
for meet in meets:
    if meet[0] >= prev_end:
        cnt += 1
        prev_end = meet[1]

print(cnt)