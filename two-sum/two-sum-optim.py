from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for num, i in enumerate(nums):
          complement = target - i
          if complement in numsMap:
            return [numsMap[complement], num]
          numsMap[i] = num
        return []  

s = Solution()
resp = s.twoSum([2,3,4], 6)
print(resp)
