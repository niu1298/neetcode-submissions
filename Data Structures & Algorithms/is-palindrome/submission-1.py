class Solution:
    def isPalindrome(self, s: str) -> bool:

        t = ""

        for ch in s:
            if ch.isalnum():
                t += ch.lower()

        n = len(t)

        if t==t[::-1]:
            return True
        else:
            return False