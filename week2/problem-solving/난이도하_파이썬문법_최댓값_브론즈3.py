# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
arr = [int(input()) for _ in range(9)]
max_num = arr[0]
max_iter = 1
for i in range(1,9):
    if arr[i] > max_num:
        max_num = arr[i]
        max_iter = i+1
print(f"{max_num}\n{max_iter}")
