class Solution:
    def isPalindrome(self, s: str) -> bool:

        t = ""

        for ch in s:
            if ch.isalnum():
                t += ch.lower()

        n = len(t)

        for i in range(n // 2):
            if t[i] != t[-1 - i]:
                return False

        return True