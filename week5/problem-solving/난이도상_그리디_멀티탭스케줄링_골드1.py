# 그리디 - 멀티탭 스케줄링 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1700
import sys
input  = sys.stdin.readline

num_outlet, num_try = map(int, input().split())
trys = list(map(int, input().split()))

count = 0
outlet = set()
for i, itm in enumerate(trys):
    #있나
    if itm in outlet:
        continue

    #자리 있나
    if len(outlet) < num_outlet:
        outlet.add(itm)
        continue

    #자리없구만..제일 나중에 있거나 더 없는 거로
    lst_replace = []    #나중에 나오는 대로 append
    for nxt in trys[i+1:num_try]:
        if nxt in outlet:
            if nxt not in lst_replace:
                lst_replace.append(nxt)
    
    if len(lst_replace) == len(outlet):
        replace = lst_replace[-1]
    else:
        for k in outlet:
            if k not in lst_replace:
                replace = k
                break
    
    outlet.remove(replace)
    outlet.add(itm)
    count += 1

print(count)