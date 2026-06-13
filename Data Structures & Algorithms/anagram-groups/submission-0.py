class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def identify_anagram(s, t):
            s_li = sorted(list(s))
            t_li = sorted(list(t))
            if s_li == t_li:
                return True
            else:
                return False

        ans = []
        for string in strs:
            for i in range(len(ans)):
                if identify_anagram(string, ans[i][0]):
                    ans[i].append(string)
                    break
            else:
                ans.append([string])

        return ans