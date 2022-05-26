class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            n = 0
            toSubtract = divisor
            while (dividend >= toSubtract):
                toSubtract = toSubtract << 1
                n += 1
            result += 1 << (n - 1)
            dividend -= toSubtract >> 1
        result = result if sign == 1 else -result
        if result < -2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647
        return result
