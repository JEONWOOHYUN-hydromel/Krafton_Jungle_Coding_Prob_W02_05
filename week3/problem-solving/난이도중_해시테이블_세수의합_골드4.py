# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
n = int(input())
arr = sorted(int(input()) for _ in range(n))

set_sum = set()

for i in range(n):
    for j in range(i, n):
        set_sum.add(arr[i] + arr[j])


for k in arr[::-1]:
    for z in arr[::-1]:
        if (k-z) in set_sum:
            print(k)
            exit()
