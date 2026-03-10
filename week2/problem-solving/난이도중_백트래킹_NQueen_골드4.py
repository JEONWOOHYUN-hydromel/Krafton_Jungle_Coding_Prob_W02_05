# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
n = int(input())

used_col = [False] * n
used_cross_upper = [False] * (2*n-1) # row + col (2,0), (1,1) (0,2)
used_cross_lower = [False] * (2*n-1) # row - col (0,0), (1,1) (2,2)

count = 0

def dfs(row):
    global count

    #(nQueen달성!)
    if row == n:
        count += 1
        return
    
    #탐색
    for col in range(n):
        isPossible = True

        #공격권에 닿는다!
        num_upper = col + row
        num_lower = col - row + n - 1
        if used_col[col] or used_cross_upper[num_upper] or used_cross_lower[num_lower]:
            continue
        
        used_col[col] = True
        used_cross_upper[num_upper] = True 
        used_cross_lower[num_lower] = True

        dfs(row+1)

        used_col[col] = False
        used_cross_upper[num_upper] = False
        used_cross_lower[num_lower] = False

dfs(0)

print(count)