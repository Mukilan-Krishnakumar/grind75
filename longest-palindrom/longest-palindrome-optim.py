class Solution:
    def longestPalindrome(self, s: str) -> int:
        string_val = Counter(s)
        odd_val = 0
        result = 0
        for values in string_val.values():
            if values % 2 == 0:
                result += values
            else:
                odd_val = 1
                result += (values-1)
        
        return result + odd_val
