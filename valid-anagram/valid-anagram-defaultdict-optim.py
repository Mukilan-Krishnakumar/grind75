from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # default dict to handle missing keys
        count = defaultdict(int)
        for x in s:
            count[x] += 1
        for x in t:
            count[x] -= 1
        for val in count.values():
            if val!= 0:
                return False  
        return True

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
