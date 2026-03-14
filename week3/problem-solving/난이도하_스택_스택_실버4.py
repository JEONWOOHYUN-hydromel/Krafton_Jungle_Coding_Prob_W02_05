# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
num_cmd = int(input())

stack = []
result = []
for _ in range(num_cmd):
    cmd = input().split()
    
    if cmd[0] == "push":
        stack.append(cmd[1])
    
    elif cmd[0] == "pop":
        if not stack:
            result.append(-1)
        else:
            result.append(stack.pop())
            
    elif cmd[0] == "size":
        result.append(len(stack))

    elif cmd[0] == "empty":
        if not stack:
            result.append(1)
        else:
            result.append(0)
        
    elif cmd[0] == "top":
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

print("\n".join(map(str, result)))