class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in nums:
            if i not in seen:
                seen[i] = False
            else:
                seen[i] = True
                
       
        if True in seen.values():  
            return True
        
        return False