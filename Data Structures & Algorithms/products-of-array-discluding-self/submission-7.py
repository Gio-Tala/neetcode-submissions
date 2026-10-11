class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightwards_list = [1]
        for i, num in enumerate(nums):
            rightwards_list.append(rightwards_list[i]*num)
        

        leftwards_list = [1]
        for i, num in enumerate(nums[::-1]):
            leftwards_list.append(leftwards_list[i]*num)
        
        leftwards_list = leftwards_list[::-1]

        outp = []
        for i in range(len(nums)):
            outp.append(rightwards_list[i] * leftwards_list[i+1])

        return outp