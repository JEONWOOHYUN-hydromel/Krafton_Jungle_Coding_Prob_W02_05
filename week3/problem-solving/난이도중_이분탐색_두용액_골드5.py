# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
n = int(input())
arr = list(map(int, input().split()))

#분할 정복
def div_conq(arr, start, end):
    if start >= end:
        return
    
    mid = start + (end - start) // 2
    div_conq(arr, start, mid)
    div_conq(arr, mid+1, end)

    #merge
    arr_left = arr[start:mid+1]
    arr_right = arr[mid+1:end+1]

    i, j = 0, 0
    k = start
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] <= arr_right[j]:
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1

    while i < len(arr_left):
        arr[k] = arr_left[i]
        i += 1
        k += 1
    while j < len(arr_right):
        arr[k] = arr_right[j]
        j += 1
        k += 1
    return 

div_conq(arr, 0, len(arr)-1)

#투포인터
i, j = 0, n - 1
pair_min = [arr[i], arr[j]]
num_min = abs(arr[i] + arr[j])
while i < j:
    num_sum = arr[i] + arr[j]
    if num_sum == 0:
        pair_min[0] = arr[i]
        pair_min[1] = arr[j]
        break
    
    if abs(num_sum) < num_min:
        num_min = abs(num_sum)
        pair_min[0] = arr[i]
        pair_min[1] = arr[j]
    
    if num_sum < 0:
        i += 1
    else:
        j -= 1

print(pair_min[0], pair_min[1])