class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = list(set(letters))
        if target not in letters:
            letters.append(target)
        letters = sorted(letters)
        newIndex = letters.index(target) + 1
        if newIndex == len(letters):
            return letters[0]
        return letters[newIndex]