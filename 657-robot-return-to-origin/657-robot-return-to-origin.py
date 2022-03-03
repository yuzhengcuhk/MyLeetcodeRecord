class Solution:
    def judgeCircle(self, moves: str) -> bool:
        U, D, L, R = moves.count('U'), moves.count('D'), moves.count('L'), moves.count('R')
        if U == D and L == R:
            return True
        else:
            return False
        