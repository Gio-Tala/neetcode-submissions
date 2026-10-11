class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed_nums = {}

        for i, num in enumerate(nums):
            if target - num in hashed_nums:
                return [hashed_nums[target - num], i]
            hashed_nums[num] = i