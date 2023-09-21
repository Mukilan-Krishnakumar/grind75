from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ctr_s = Counter()
        ctr_t = Counter()
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        for i in range(len_s):
            ctr_s[s[i]] += 1
            ctr_t[t[i]] += 1
        if ctr_s != ctr_t:
            return False
        else:
            return True

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
