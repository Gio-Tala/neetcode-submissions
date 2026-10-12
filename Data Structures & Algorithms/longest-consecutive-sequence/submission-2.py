class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check for first element
        if len(nums) == 0:
            return 0
        set_nums = set(nums)
        max_len = 1
        for num in set_nums:
            if num - 1 in set_nums:
                continue

            curr_len = 1
            # num - 1 not in set_nums. it's beginning of sequence
            while num + 1 in set_nums:
                num += 1
                curr_len += 1

            if curr_len > max_len:
                max_len = curr_len
        
        return max(max_len, curr_len)