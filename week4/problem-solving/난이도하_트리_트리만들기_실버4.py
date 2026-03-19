# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
total, leaf_num = map(int, input().split())
turn = total-leaf_num+1

for i in range(total):
    if i < turn:
        print(i, i+1)
    elif i > turn:
        dif = i - turn
        if i-dif < 2:
            print(0, i)
        else:
            print(i-dif-1 , i)