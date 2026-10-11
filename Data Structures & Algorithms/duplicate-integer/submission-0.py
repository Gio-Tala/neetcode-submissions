class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashedNums = set()
        for num in nums:
            if num in hashedNums:
                return True
            else:
                hashedNums.add(num)
        
        return False