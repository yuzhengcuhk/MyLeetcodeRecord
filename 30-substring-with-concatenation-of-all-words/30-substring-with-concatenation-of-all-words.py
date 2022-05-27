class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def splitWindow(winS, windowLength, wordLength):
            return [winS[i: i+wordLength] for i in range(0, windowLength, wordLength)]
        
        wordLength = len(words[0])
        wordSet = set(words)
        sLength = len(s)
        windowLength = wordLength * len(words)
        sortExactWindow = ''.join(sorted(words))
        result = []
        for i in range(sLength - windowLength + 1):
            if s[i:i+wordLength] in wordSet:
                currentMatch = ''.join(sorted(splitWindow(s[i:i+windowLength], windowLength, wordLength)))
                if currentMatch == sortExactWindow:
                    result.append(i)
        return result