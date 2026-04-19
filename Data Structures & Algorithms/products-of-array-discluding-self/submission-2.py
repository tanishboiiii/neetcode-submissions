class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        prod = 1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                zero_index = i
            else:
                prod *= nums[i]

        if zero_count > 1:
            return [0]*len(nums)
        elif zero_count == 1:
            ans = [0] * len(nums)
            ans[zero_index] = prod
            return ans
        else:
            ans = [prod]*len(nums)
            
            for i in range(len(nums)):
                ans[i] = int(ans[i] / nums[i])

            return ans
        
