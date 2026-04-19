class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prod, zero_cnt = 1, 0

        # if there is 1 zero, then ans is always zero except on one instance
        # if there is more than 1 zero, ans is arr of 0's

        for i in nums:
            if i:
                prod *= i
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return [0]*len(nums)
        
        for i in nums:
            # if i = 0, then append the prod 
            # if i is not 0 and the zero_cnt == 1, then append 0
            # if i is not 0 and no zero's, then append prod/i
            
            if i == 0:
                ans.append(prod)
            else:
                if zero_cnt == 1:
                    ans.append(0)
                else:
                    ans.append(int(prod/i))
            
        return ans