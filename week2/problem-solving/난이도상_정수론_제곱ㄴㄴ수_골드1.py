# 정수론 - 제곱 ㄴㄴ 수 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1016
min_num, max_num = map(int, input().split())
check = [False] * (max_num - min_num + 1)

i = 2
while i**2 <= max_num:
    sq = i**2
    for j in range((min_num//sq)-1, (max_num//sq)+1):
        num = j * sq
        if min_num <= num <= max_num:
            check[num - min_num] = True
    i += 1

print(check.count(False))