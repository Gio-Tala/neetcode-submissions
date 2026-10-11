class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outp = []
        total_product = 1
        num_zeros = 0

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                num_zeros += 1
        
        for num in nums:
            if num_zeros >= 2:
                outp.append(0)
            elif num_zeros == 1:
                if num == 0:
                    outp.append(total_product)
                else:
                    outp.append(0)
            else:
                outp.append(total_product // num)
        
        return outp
            
        