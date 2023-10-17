class Solution:
    '''
        oddCount is a variable which tracks the number of odd values. 
        We are checking in each iteration if the current mapping value is odd 
        or even and update this counter based on this. All even values 
        contribute nothing to this counter but odd values do.
        Interestingly, the pattern is this:
        Longest Palindrome = length of string - odd count (total number of odd values) + 1
    '''
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
