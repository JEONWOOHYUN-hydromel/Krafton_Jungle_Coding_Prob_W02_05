# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
exp_num = int(input())

def isPrime(n):
    if n==2:
        return True
    if not n%2:
        return False
    for i in range(3,int(n**0.5+1),2):
        if not n%i:
            return False
    return True

def next_P(n):
    while True:
        next_num = n+1
        if isPrime(next_num):
            return next_num
        n=next_num
    
def gold_B(n):
    a = 2
    while True:
        b = n - a
        if b < a:
            break
        if isPrime(b):
            gold_case.append([a,b])
        a = next_P(a)
    return

for _ in range(exp_num):
    gold_case= []
    gold_B(int(input()))
    min_case = gold_case[0]
    min_gap = gold_case[0][1] - gold_case[0][0]
    for case in gold_case:
        gap = case[1] - case[0]
        if gap < min_gap:
            min_case = case
            min_gap = gap
    print(min_case[0], min_case[1])

