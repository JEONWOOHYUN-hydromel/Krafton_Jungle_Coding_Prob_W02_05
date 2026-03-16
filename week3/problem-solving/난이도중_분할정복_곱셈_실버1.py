# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
num_input = list(map(int, input().split()))
A = num_input[0]
B = num_input[1]
C = num_input[2]

def power(a,b):
    if b == 1 :
        return a % C
    
    h = power(a, b//2)

    if b % 2:
        return (h*h*a) % C
    else: 
        return (h*h) % C
    
print(power(A,B))