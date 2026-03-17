# 링크드리스트 - malloc (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/3217
import sys
input = sys.stdin.readline

n = int(input())

dic = {}
mem = []
mem_size = 100000
for _ in range(n):
    line = input().replace("=", " ").replace("(", " ").replace(")", " ")
    cmd = line.split()
    if "malloc" in cmd:
        var = cmd[0]
        size = int(cmd[2])

        if not mem:
            mem_loc = [1, size]
            dic[var] = mem_loc
            mem.append(mem_loc)
        else: 
            start = 1
            for located in mem:
                if start+size-1 < located[0]:
                    break
                else:
                    start = located[1] + 1

            if start+size-1 > mem_size:
                dic[var] = None

            else:
                mem_loc = [start, start+size-1]
                dic[var] = mem_loc
                mem.append(mem_loc)
                mem.sort()
        

    elif "free" in cmd:
        var = cmd[1]
        mem_free = dic.get(var)
        if mem_free is not None:
            mem.remove(mem_free)
        dic[var] = None
    
    elif "print" in cmd:
        var = cmd[1]
        find_var = dic.get(var)
        if find_var != None:
            print(find_var[0])
        else:
            print(0)