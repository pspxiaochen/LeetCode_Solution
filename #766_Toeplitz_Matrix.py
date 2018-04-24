def isToeplitzMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            row = i
            columns = j
            s = matrix[i][j]
            while row < len(matrix) and columns < len(matrix[0]):
                if s != matrix[row][columns]:
                    return False
                else:
                    row += 1
                    columns += 1
    return True

def isToeplitzMatrix_2(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True