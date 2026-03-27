# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num_cand = int(input())
    lst_cand = [list(map(int, input().split())) for _ in range(num_cand)]

    lst_cand.sort(key= lambda x:(x[0], x[1]))

    cnt = 1
    b_least = lst_cand[0][1]
    for cand in lst_cand[1:]:
        if cand[1] < b_least:
            cnt += 1
            b_least = cand[1]
    
    print(cnt)