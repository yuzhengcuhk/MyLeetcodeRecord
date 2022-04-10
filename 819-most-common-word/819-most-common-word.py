class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paraList = re.split('\W', paragraph.lower())
        paraListAlpha = []
        for item in paraList:
            item = ''.join([i for i in item if i.isalpha()])
            paraListAlpha.append(item)
        countParaList = Counter(paraListAlpha)
        countParaListSort = sorted(countParaList.items(), key = lambda x:x[1], reverse=True)
        print(countParaListSort)
        for item in countParaListSort:
            if item[0] in banned or item[0] == '':
                continue
            return item[0]
        