class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.li = stones
        
        while len(self.li)>1:
            self.li.sort()
            x = self.li.pop()
            y = self.li.pop()

            if x!= y:
                self.li.append(x-y)
            
            # self.li.sort()
        
        if len(self.li) == 1:
            return self.li[0]

        else:
            return 0