class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        for item in ops:
            if item == "C":
                score.pop()
            elif item == "+":
                score.append(int(score[-1]) + int(score[-2]))
            elif item == "D":
                score.append(2*int(score[-1]))
            else:
                score.append(int(item))
        return sum(score)
                