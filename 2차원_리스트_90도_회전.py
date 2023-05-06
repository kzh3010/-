def rotate_90(a) :
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result 