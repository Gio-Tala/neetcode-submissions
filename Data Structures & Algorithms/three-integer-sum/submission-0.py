class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 pointers of only following elements because we don't have to look at past elements cuz wouldve already been inluded

        # sort these elements
        sorted_nums = sorted(nums)
        outp_set = set()
        outp = []
        for i in range(len(sorted_nums)):
            curr_target = -1 * sorted_nums[i]
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                curr_two_sum = sorted_nums[left] + sorted_nums[right]
                if curr_two_sum == curr_target:
                    if tuple([sorted_nums[i], sorted_nums[left], sorted_nums[right]]) not in outp_set:
                        outp.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                        outp_set.add(tuple([sorted_nums[i], sorted_nums[left], sorted_nums[right]]))
                    right -= 1
                elif curr_two_sum > curr_target:
                    right -= 1
                else:
                    left += 1
        
        return list(outp)