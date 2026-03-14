# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

first_string = input().rstrip()
num_cmd = int(input())

front_stack = list(first_string)
back_stack = []

for _ in range(num_cmd):
    cmd = input().split()
    
    if cmd[0] == "L":
        if front_stack:
            back_stack.append(front_stack.pop())

    elif cmd[0] == "D":
        if back_stack:
            front_stack.append(back_stack.pop())

    elif cmd[0] == "B":
        if front_stack:
            front_stack.pop()

    elif cmd[0] == "P":
        front_stack.append(cmd[1])

while back_stack:
    front_stack.append(back_stack.pop())

print("".join(front_stack))
