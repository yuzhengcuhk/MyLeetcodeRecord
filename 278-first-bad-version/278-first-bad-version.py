# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while 1:
            check = start + (end - start) // 2
            if isBadVersion(check) == False:
                start = check + 1
            elif isBadVersion(check-1) == False:
                return check
            else:
                end = check - 1