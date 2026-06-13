class MedianFinder:

    def __init__(self):
        self.li = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.li.append(num)
        self.n += 1
        self.li.sort()

    def findMedian(self) -> float:
        if self.n%2 == 0:
            return (self.li[self.n//2]+self.li[self.n//2-1])/2
        else:
            return self.li[self.n//2]
        