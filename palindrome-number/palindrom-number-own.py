class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_a = str(x)
        string_b = string_a[::-1]
        if string_a == string_b:
            return True
        else:
            return False
