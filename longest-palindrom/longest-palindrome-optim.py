class Solution:
    '''
    Using Counter, we have the frequencies. We go through the values, if odd, we take only the even value and keep the odd counter as 1. Palindrom = all_even_val + closest_even_to_odd + odd_val (1 if odd is present, else 0).
    '''
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
