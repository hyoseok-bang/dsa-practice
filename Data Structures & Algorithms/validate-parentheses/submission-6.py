class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        if len(s) % 2 != 0:
            return False

        for p in s:
            if p in bracket_pairs:
                if len(stack) == 0 or stack[-1] != bracket_pairs[p]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(p)
        
        if len(stack) == 0:
            return True
        else:
            return False
                    