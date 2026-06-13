class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_temp = sorted(list(s))
        t_temp = sorted(list(t))
        if s_temp == t_temp:
            return True
        else:
            return False