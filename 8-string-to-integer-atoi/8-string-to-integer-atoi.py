class Solution:
    def myAtoi(self, s: str) -> int:
        pureS = s.strip()
        if not pureS:
            return 0
        result = re.findall(r"^[+-]?\d+", pureS)
        if not result:
            return 0
        return max(min(int(result[0]), 2**31-1), -2**31)