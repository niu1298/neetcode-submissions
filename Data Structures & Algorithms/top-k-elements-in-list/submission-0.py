class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for num in nums:
            if num in dic.keys():
                dic[num]+=1
            else:
                dic[num] = 1
        ans = []
        for i in range(k):
            # count = dic.values().index(max(dic.values()))
            # ans.append(dic.keys()[i])
            key = max(dic, key=dic.get)
            ans += [key]
            del dic[ans[-1]]
        return ans