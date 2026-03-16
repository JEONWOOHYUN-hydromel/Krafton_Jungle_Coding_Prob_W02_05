# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493
n = int(input())
towers = list(map(int, input().split()))

stack = []
result = []
for i in range(n):
    while stack and towers[stack[-1]] <= towers[i]:
        stack.pop()

    if stack:
        result.append(stack[-1] + 1)
    else:
        result.append(0)

    stack.append(i)

print(" ".join(map(str, result)))