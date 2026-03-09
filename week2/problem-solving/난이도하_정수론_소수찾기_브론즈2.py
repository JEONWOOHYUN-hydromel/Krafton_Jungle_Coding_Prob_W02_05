# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
n = int(input())
arr = list(map(int, input().split()))
prime_count = 0
for num in arr:
    if num == 2:
        prime_count+=1
        continue
    elif num < 2 or not num%2:
        continue
    else:
        isPrime = True
        for i in range(3, int(num**0.5)+1, 2):
            if not num%i:
                isPrime = False
                   
        if isPrime:
            prime_count+=1
print(prime_count)
