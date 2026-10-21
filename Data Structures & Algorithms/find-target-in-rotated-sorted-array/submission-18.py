class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # must find front of list
        lo = 0
        hi = len(nums) - 1
        mid = (lo + hi) // 2

        while lo <= hi:
            
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid

            print("hi", hi, "lo", lo, "mid", mid)

            if nums[lo] <= nums[mid]:
                # left side sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # right side sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1 
            
            print("2hi", hi, "lo", lo, "mid", mid)

        if nums[hi] == target:
            return hi    
        return -1
            
            
            

