class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digSet = {'2': 'abc',
                  '3': 'def',
                  '4': 'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz'}
        def backTracking(currComb, level):
            if level == len(digits):
                results.append(currComb)
                return 
            for alpha in digSet[digits[level]]:
                backTracking(currComb+alpha, level+1)
                
        if not digits:
            return []
        results = []
        backTracking('', 0)
        return results