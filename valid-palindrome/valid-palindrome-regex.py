import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_pattern = r'\W|(_)'
        word_sub = re.compile(word_pattern)
        removed_char = re.sub(word_sub,"", s)
        removed_char = removed_char.lower()
        check_str = removed_char[::-1]
        if removed_char == check_str:
            return True
        else:
            return False

s = Solution()
resp = s.isPalindrome("A man, a plan, a canal: Panama")
print(resp)
