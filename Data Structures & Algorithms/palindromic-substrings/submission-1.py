class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        if n == 1:
            return 1

        resLen = 0
        start = 0


        num = 0

        def extend(l,r):
            nonlocal resLen, start, num

            while l >= 0 and r < n:
                if s[l] == s[r]:
                    curr_l = r-l+1
                    # if curr_l > resLen:
                    #     resLen = curr_l
                    #     start = l
                    num += 1
                    l-=1
                    r+=1
                else:
                    break
                    
        for i in range(n):
            extend(i,i)
            extend(i,i+1)
            # print(s[start:start+resLen])

        return num


