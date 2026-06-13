class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.li = nums
        self.k = k
        return None

    def add(self, val: int) -> int:
        self.li.append(val)
        self.li.sort()

        return self.li[-1-(self.k-1)]
