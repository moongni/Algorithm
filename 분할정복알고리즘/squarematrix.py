"""
    행렬의 거듭제곱
    n x n 크기의 행렬 A의 거듭제곱 A^m은 A를 m번 연속해서 곱한것임
    시간복잡도는 (n^3m)임

    A^m = A^m/2 x A^m/2
"""
"""
    1, 2, 3,     1, 2, 3,
    4, 5, 6,     4, 5, 6,
    7, 8, 9,     7, 8, 9,
"""
def square_identity(m):
    ret = [[ 0 for _ in range(m)] for _ in range(m)]
    
    for i in range(m):
        ret[i][i] = 1
    
    return ret

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def square_mul(matrix1, matrix2):
    # 두 행렬 차수 확인
    if len(matrix1) != len(matrix2):
        raise TypeError()

    n = len(matrix1)
    ret = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return ret

def square_pow(matrix, m):
    n = len(matrix)

    # 기저조건
    if m == 0: return square_identity(n)

    # m이 홀수일 경우    
    if n % 2 == 1: return square_mul(square_pow(matrix, m - 1), matrix)

    half = square_pow(matrix, m / 2)

    return square_mul(half, half)

mat = [
[2, 0, 0],
[0, 2, 0],
[0, 0, 2]
]

print_matrix(square_pow(mat, 31))