# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

plate_num = int(input())
cnt = 0

def move(from_, to_):
    global cnt
    print(from_, to_)
    cnt+=1

def run_hanoi(n, str, tmp, end):
    if n == 1:
        move(str, end)
        return
    run_hanoi(n-1, str, end, tmp)
    move(str, end)
    run_hanoi(n-1, tmp, str, end)

print(2**plate_num-1)
if plate_num <= 20:
    run_hanoi(plate_num, 1, 2, 3)
# print(cnt)