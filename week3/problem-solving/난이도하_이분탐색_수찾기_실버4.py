# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()

def binary_search(start, end, target):
    if start > end:
        return False
    elif start == end:
        if target == n_arr[start]:
            return True
        else: 
            return False
    else:
        mid = start + (end - start) // 2
        if n_arr[mid] == target:
            return True
        elif n_arr[mid] > target:
            return binary_search(start, mid-1, target)
        else:
            return binary_search(mid+1, end, target)
        
for num in m_arr:
    if binary_search(0, n-1, num):
        print(1)
    else:
        print(0)