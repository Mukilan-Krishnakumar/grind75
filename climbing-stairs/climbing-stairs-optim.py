# NeetCode Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic Programming using two variables following fibonacci Series
        one, two = 1, 1
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one
            
