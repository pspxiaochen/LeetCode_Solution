import numpy as np
def isValidSudoku(board):
    rows = np.zeros((9,9))
    cols = np.zeros((9,9))
    blocks = np.zeros((9,9))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '.':
                num = int(board[i][j]) - 1
                k = i // 3 * 3 + j // 3
                if rows[i][num] or cols[j][num] or blocks[k][num]:
                    return False
                rows[i][num] = cols[j][num] = blocks[k][num] = 1
    return True
