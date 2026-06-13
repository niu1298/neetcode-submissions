class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        resLen = 0

        def expand(l, r):
            nonlocal res, resLen

            while l >= 0 and r < n and s[l] == s[r]:
                currLen = r - l + 1

                if currLen > resLen:
                    resLen = currLen
                    res = s[l:r + 1]

                l -= 1
                r += 1

        for i in range(n):
            # odd length: "aba"
            expand(i, i)

            # even length: "abba"
            expand(i, i + 1)

        return res

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 1:
#             return s

#         if len(s) == 2 and s[0]==s[1]:
#             return s

#         def is_palindrome(st):
#             if st =="":
#                 return True
#             half = len(st)//2
#             if len(st)%2 == 1:
#                 return is_palindrome(st[0:half]+st[half+1:])
            
#             for i in range(0,half):
#                 if st[i] != st[-i-1]:
#                     return False

#             return True


#         def extend(index):
#             temp = s[index]
            
#             index_l = index
#             index_r = index+1
#             contin = True
#             while (index_l>=0 or index_r < n) and contin:
#                 if index_l-1>=0 and index_r+1 <= n and s[index_l-1] == s[index_r]:
#                     index_l -= 1
#                     index_r += 1
#                     continue
                
#                 if index_l-1>=0:
#                     if is_palindrome(s[index_l-1:index_r]): #s[index_l-1] == s[index_r]: #is_palindrome(s[index_l-1:index_r]):
#                         index_l -= 1
#                         continue
#                 if index_r+1 <= n:
#                     if is_palindrome(s[index_l:index_r+1]): #s[index_l] == s[index_r+1]: #is_palindrome(s[index_l:index_r+1]):
#                         index_r += 1
#                         continue
#                 break
#             return (index_l,index_r)
   
#         resLen = 0
#         start = 0

#         n = len(s)

#         for i in range(n):
#             temp = extend(i)
#             length = temp[1]-temp[0]
#             if length >= resLen:
#                 resLen = length
#                 start = temp[0]
            
#         return s[start:start+resLen]

                


