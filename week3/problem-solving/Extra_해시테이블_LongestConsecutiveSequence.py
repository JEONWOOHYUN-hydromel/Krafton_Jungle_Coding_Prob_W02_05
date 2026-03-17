# 해시 테이블 - Longest Consecutive Sequence
# 문제 링크: https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150

num = [0,3,7,2,5,8,4,6,0,1]
num.sort()
max = 0
connect = 1
cur = num[0]
for n in num:
    if n == cur:
        pass
    elif n == cur + 1:
        connect += 1
    else:
        if connect > max:
            max = connect
        connect = 1
    cur = n

if connect > max:
    max = connect
    
print(max)