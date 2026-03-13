# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
# n = int(input())
# matrix = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

n = 2
matrix = [[0, 0], [0, 1]]

#[white, blue]
num_squares = [0, 0]

def check_square(mat, x, y, n):
    isSquare = True
    color = mat[x][y]
    for i in range(n):
        for j in range(n):
            nx = x+i
            ny = y+j

            if mat[nx][ny] != color:
                return False
    
    return True

def div_conq(mat, x, y, n):
    if n == 1:
        num_squares[mat[x][y]] += 1
        return
    
    if check_square(mat, x, y, n):
        num_squares[mat[x][y]] += 1
    else:
        half = n//2
        div_conq(mat, x, y, half)
        div_conq(mat, x+half, y, half)
        div_conq(mat, x, y+half, half)
        div_conq(mat, x+half, y+half, half)

    return        

div_conq(matrix, 0, 0, n)
print(num_squares[0])
print(num_squares[1])