class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[hi] < nums[hi - 1]:
                return nums[hi]

            if nums[mid] > nums[hi]:
                lo = mid
            else:
                hi = mid
        
        return nums[hi]
