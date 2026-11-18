class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2 possible maxes at any specific point
        # max(i-1), or max(i-2) + nums[i]
        hashed_ways = {}
        def count_ways(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i not in hashed_ways:
                hashed_ways[i] = max(count_ways(i - 1), nums[i] + count_ways(i - 2))
            
            return hashed_ways[i]

        return count_ways(len(nums) - 1)