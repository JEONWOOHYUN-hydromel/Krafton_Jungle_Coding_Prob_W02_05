# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
l1 = len(str1)
l2 = len(str2)

arr = [[0]*(l1+1) for _ in range(l2+1)]

for i in range(1, l2+1):
    for j in range(1, l1+1):
        if str1[j-1] == str2[i-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[l2][l1])