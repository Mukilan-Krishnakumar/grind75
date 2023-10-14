class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = bin(int(a,2) + int(b,2))
        return output[2:]
