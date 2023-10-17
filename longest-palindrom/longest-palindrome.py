class Solution:
    def longestPalindrome(self, s: str) -> int:
        oddCount = 0
        char_map = {}
        for i in s:
            if i in char_map:
                char_map[i] += 1
            else:
                char_map[i] = 1

            if char_map[i] %2 != 0:
                oddCount += 1
            else:
                oddCount -= 1
        
        if oddCount > 1:
            return len(s) - oddCount + 1
        else:
            return len(s)
