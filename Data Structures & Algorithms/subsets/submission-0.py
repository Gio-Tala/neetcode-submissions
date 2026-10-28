class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        outp = []

        curr_subset = []
        def backtracking_dfs(i):
            # if just past root
            if i == len(nums):
                outp.append(curr_subset.copy())
                return

            curr_subset.append(nums[i])
            backtracking_dfs(i+1)

            curr_subset.pop()
            backtracking_dfs(i+1)
            
        backtracking_dfs(0)
        return outp