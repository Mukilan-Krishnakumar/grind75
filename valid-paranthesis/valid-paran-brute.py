class Solution:
    def isValid(self, s: str) -> bool:
        open_paranthesis = {"(" : 1, "[": 2, "{": 3}
        closed_paranthesis = {")" : 1, "]" : 2, "}" : 3}
        stack = []
        if len(s) > 1:
            for i in s:
                if i in open_paranthesis:
                    stack.append(open_paranthesis[i])
                else:
                    if len(stack) == 0:
                        return False
                    else:
                        if closed_paranthesis[i] != stack[-1]:
                            return False
                        else:
                            stack = stack[:-1]
            if len(stack) > 0:
                return False
        else:
            return False
        return True

s = Solution()
resp = s.isValid("(()")
print(resp)
