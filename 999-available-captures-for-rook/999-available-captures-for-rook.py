class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        xRook = 0  # find location of R
        yRook = 0
        flag = False
        for i in range(8):
            if flag:
                break
            for j in range(8):
                if board[i][j] == 'R':
                    xRook = i
                    yRook = j
                    flag = True
                    break
        result = 0
        for k in range(1, xRook+1):
            if board[xRook-k][yRook] == 'p':
                result += 1
                break
            elif board[xRook-k][yRook] == 'B':
                break
        for k in range(1, yRook+1):
            if board[xRook][yRook-k] == 'p':
                result += 1
                break
            elif board[xRook][yRook-k] == 'B':
                break
        for k in range(1, 8-xRook):
            if board[xRook+k][yRook] == 'p':
                result += 1
                break
            elif board[xRook+k][yRook] == 'B':
                break
        for k in range(1, 8-yRook):
            if board[xRook][yRook+k] == 'p':
                result += 1
                break
            elif board[xRook][yRook+k] == 'B':
                break
        return result