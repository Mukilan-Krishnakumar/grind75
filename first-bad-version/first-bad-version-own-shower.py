# Came up with this while showering, crazy innit
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        mid = (start + end)//2
        rep = -1
        while start <= end:
            if start == mid == end:
                return mid
            elif isBadVersion(mid) == False:
                start = mid + 1
            elif isBadVersion(mid) == True:
                end = mid
            mid = (start + end)//2
        return rep
