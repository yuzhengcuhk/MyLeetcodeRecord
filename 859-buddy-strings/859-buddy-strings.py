class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        '''
        if len(s) != len(goal): return False
        Two possible cases:
            1. if s == goal: repeated letters in s
            2. is two different letters between s and goal: exchange them and see if s == goal
        '''
        if len(s) != len(goal):
            return False
        diffLetterS = []
        diffLetterG = []
        for i, item in enumerate(s):
            if goal[i] != item:
                diffLetterS.append(item)
                diffLetterG.append(goal[i])
        print(diffLetterS, diffLetterG)
        if len(diffLetterS) == 0:
            return len(set(s)) < len(s)
        elif len(diffLetterS) == 2:
            if (diffLetterS[0] == diffLetterG[1]) and (diffLetterS[1] == diffLetterG[0]):
                return True
        else:
            return False