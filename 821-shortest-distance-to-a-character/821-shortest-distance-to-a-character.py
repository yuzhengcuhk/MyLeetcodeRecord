class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        cIndex = [i for i in range(len(s)) if s[i] == c]
        for i in range(len(s)):
            distRecord = [abs(j-i) for j in cIndex]
            answer.append(min(distRecord))
        return answer
            
        