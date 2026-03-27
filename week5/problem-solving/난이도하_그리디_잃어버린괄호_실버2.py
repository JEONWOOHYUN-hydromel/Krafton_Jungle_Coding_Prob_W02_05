# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
s = input()

nums = []
ops = []
num = ""

for ch in s:
    if ch.isdigit():
        num+=ch
    else:
        nums.append(int(num))
        num = ""
        ops.append(ch)

nums.append(int(num))

minusOn = False
total = nums[0]
for i, op in enumerate(ops):
    if minusOn:
        total -= nums[i+1]
        continue

    if op == "+":
        total += nums[i+1]
    elif op == "-":
        minusOn = True
        total -= nums[i+1]

print(total)