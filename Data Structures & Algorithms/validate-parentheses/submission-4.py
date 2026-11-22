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
            if p in bracket_pairs.values():
                stack.append(p)
            if p in bracket_pairs:
                if len(stack) == 0:
                    return False
                if stack[-1] == bracket_pairs[p]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
                    