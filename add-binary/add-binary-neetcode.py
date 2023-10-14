class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        a, b = a[::-1], b[::-1]
        carry = 0

        for i in range(max(len(a), len(b))):
            digA = ord(a[i]) - ord("0") if i < len(a) else 0
            digB = ord(b[i]) - ord("0") if i < len(b) else 0
            total = digA + digB + carry
            char = str(total%2)
            res = char + res
            carry = total//2
        
        if carry:
            res = "1" + res
        return res
