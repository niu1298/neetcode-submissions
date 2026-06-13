class Solution:
    def search(self, nums: List[int], target: int) -> int:
        find = False
        start = 0
        end = len(nums)
        mid = end//2
        while find == False:
            if nums[mid] == target:
                find = True
                return mid
            if nums[start] == target:
                return start
            if nums[mid] > target:
                end = mid
                mid = (start+end)//2
            if nums[mid] < target:
                start = mid
                mid = (start+end)//2
            if mid== start or mid == end or end == start:
                find = True
                return -1

