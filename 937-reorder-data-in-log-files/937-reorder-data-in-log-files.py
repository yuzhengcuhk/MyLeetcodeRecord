class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digList = []
        letList = []
        for log in logs:
            item = log.split(" ")
            if item[1].isalpha():
                letList.append((' '.join(item[1:]), item[0]))
            else:
                digList.append(log)
        letList.sort()
        return [letter[1] + ' ' + letter[0] for letter in letList] + digList