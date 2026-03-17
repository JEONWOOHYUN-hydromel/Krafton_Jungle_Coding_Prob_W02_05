# 스택 - 원 영역 (백준 플래4)
# 문제 링크: https://www.acmicpc.net/problem/10000
import sys
input = sys.stdin.readline

n = int(input())

events = []
for _ in range(n):
    x, r = map(int, input().split())
    l = x - r
    rr = x + r

    events.append((l, 1, -rr))  # start
    events.append((rr, 0, -l))  # end

events.sort()

result = 1
stack = []
for event in events:
    loc = event[0]
    #start
    if event[1] == 1:
        stack.append([loc, loc]) #[start,last]
    
    #end
    elif event[1] == 0:
        result+=1
        cur = stack.pop()

        if cur[1] == loc:
            result += 1

        if stack:
            if stack[-1][1] == cur[0]:
                stack[-1][1] = loc
            

print(result)