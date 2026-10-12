class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums_set = set(nums)
        max_len = 1
        curr_len = 1
        curr_num = nums_set.pop()
        target_left = curr_num - 1
        target_right = curr_num + 1

        while len(nums_set) > 0:
            if (target_left in nums_set):
                nums_set.remove(target_left)
                target_left -= 1
                curr_len += 1
            elif (target_right in nums_set):
                nums_set.remove(target_right)
                target_right += 1
                curr_len += 1
            else:
                if curr_len > max_len:
                    max_len = curr_len
                curr_num = nums_set.pop()
                target_left = curr_num - 1
                target_right = curr_num + 1
                curr_len = 1
        

        return max(max_len, curr_len)