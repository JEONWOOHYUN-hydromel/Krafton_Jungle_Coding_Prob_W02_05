# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
case_num = int(input())
for i in range(case_num):
    arr = input().split()
    rep_num = int(arr[0])
    input_str = arr[1]
    for char in input_str:
        print(char*rep_num, end="")
    print("")
