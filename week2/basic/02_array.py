"""
[배열 - 2차원 배열 회전]

문제 설명:
- N x N 크기의 2차원 배열을 시계방향으로 90도 회전시킵니다.
- 배열의 인덱스 변환 규칙을 이해하는 문제입니다.

입력:
- matrix: N x N 크기의 2차원 리스트

출력:
- 시계방향으로 90도 회전된 2차원 리스트

예제:
입력:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

출력:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

힌트:
- 회전 후 위치: (i, j) -> (j, n-1-i)
- 새로운 배열을 만들어 값을 채워넣으세요
"""

def rotate_matrix_90(matrix):
    """
    2차원 배열을 시계방향으로 90도 회전
    
    Args:
        matrix: N x N 2차원 리스트
    
    Returns:
        회전된 2차원 리스트
    """
    n = len(matrix)
    
    # TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화)
    rotated = []
    for i in range(n):
        rotated.append([])
        for j in range(n):
            rotated[i].append(0)

    # TODO: 원본 배열의 각 요소를 회전된 위치에 배치하세요
    # 힌트: (i, j) 위치의 요소는 회전 후 (j, n-1-i) 위치로 이동

    #[y][x]
    i = 0
    try_num = n//2
    while try_num > 0:
        max_n = n-1-(2*i)
        for j in range(max_n): 
            #좌
            rotated[i+j][i] = matrix[max_n+i][i+j]
            #하
            rotated[max_n+i][i+j] = matrix[i+max_n-j][i+max_n]
            #우
            rotated[i+max_n-j][i+max_n] = matrix[i][i+max_n-j]
            #상
            rotated[i][i+max_n-j] = matrix[i+j][i]
        
        i += 1
        try_num -= 1
    if n%2:
        center = n//2
        rotated[center][center] = matrix[center][center]

    return rotated

def print_matrix(matrix):
    """배열을 보기 좋게 출력하는 헬퍼 함수"""
    for row in matrix:
        print(row)

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 3x3 배열
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("원본 배열:")
    print_matrix(matrix1)
    print("\n회전 후:")
    rotated1 = rotate_matrix_90(matrix1)
    print_matrix(rotated1)
    print()
    
    # 테스트 케이스 2: 4x4 배열
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print("원본 배열:")
    print_matrix(matrix2)
    print("\n회전 후:")
    rotated2 = rotate_matrix_90(matrix2)
    print_matrix(rotated2)


