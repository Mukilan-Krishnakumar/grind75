class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ''
        for c in s.lower():
            if c.isalnum():
                tmp += c
        return tmp == tmp[::-1]

s = Solution()
resp = s.isPalindrome("A man, a plan, a canal: Panama")
print(resp)
