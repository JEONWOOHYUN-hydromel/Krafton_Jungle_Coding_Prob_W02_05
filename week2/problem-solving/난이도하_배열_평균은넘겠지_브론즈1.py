# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
case_num = int(input())
for i in range(case_num):
    arr = list(map(int, input().split()))
    
    score_num = arr.pop(0)
    total = 0
    #합계
    for score in arr:
        total += score
    #평균
    score_avg = total / len(arr)
    #평균이상 구하기
    over_avg = 0
    for score in arr:
        if score > score_avg:
            over_avg += 1
    
    print(f"{over_avg/len(arr)*100:.3f}%")
