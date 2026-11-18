class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # bin search
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] <  nums[(mid - 1) % len(nums)]:
                return nums[mid]
            if nums[mid] < nums[len(nums) - 1]:
                hi = mid - 1
            else:
                lo = mid + 1
        return 0