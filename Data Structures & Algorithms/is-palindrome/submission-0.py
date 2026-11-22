class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_check = [c for c in s.lower() if c.isalnum()]
        print(s_check, s)
        return s_check == s_check[::-1]
