class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindrome
        if x < 0:
            return False

        reversed_n = 0
        temp = x

        while temp!= 0:
            digit = temp % 10
            reversed_n = reversed_n * 10 + digit
            temp //= 10

        return reversed_n == x
