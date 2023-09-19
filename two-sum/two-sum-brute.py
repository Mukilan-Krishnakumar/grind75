from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for enum_1, first_num in enumerate(nums):
          for enum_2, second_num in enumerate(nums):
            if enum_1 != enum_2 and first_num + second_num == target:
              return sorted([enum_1, enum_2])

s = Solution()
resp = s.twoSum([2,3,4], 6)
print(resp)
