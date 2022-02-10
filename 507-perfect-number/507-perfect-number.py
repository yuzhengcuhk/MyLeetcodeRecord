class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisorSet = []
        if num == 1:
            return False
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                if i not in divisorSet:
                    divisorSet.append(i)
                if num//i not in divisorSet:
                    divisorSet.append(num//i)
        return (num-1) == sum(divisorSet)
                