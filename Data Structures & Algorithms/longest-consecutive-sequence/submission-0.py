class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in numSet:
            if i-1 not in numSet: # this is a possible sequence start
                length = 1
                # note that i is the start of a sequence.

                while i + length in numSet: # build a sequence
                    length += 1
                
                longest = max(longest, length)

        return longest
        

    