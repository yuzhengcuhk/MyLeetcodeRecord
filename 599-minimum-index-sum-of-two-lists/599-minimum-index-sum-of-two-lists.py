class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minIndexSum = math.inf
        result = []
        for i in range(len(list1)):
            if list1[i] in list2:
                if i+list2.index(list1[i]) < minIndexSum:
                    result = [list1[i]]
                    minIndexSum = i+list2.index(list1[i])
                elif i+list2.index(list1[i]) == minIndexSum:
                    result.append(list1[i])
                else:
                    continue
        return result