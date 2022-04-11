class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowelSet = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sentList = sentence.split(' ')
        for i in range(len(sentList)):
            if sentList[i][0] in vowelSet:
                sentList[i] += 'ma' + (i + 1) * 'a'
            elif sentList[i][0] not in vowelSet:
                sentList[i] = sentList[i][1::] + sentList[i][0]
                sentList[i] += 'ma' + (i + 1) * 'a'
        return ' '.join(sentList)
        