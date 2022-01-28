class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteDict = collections.Counter(ransomNote)
        magaDict = collections.Counter(magazine)
        for key in noteDict:
            if key not in magaDict or magaDict[key] < noteDict[key]:
                return False
        return True