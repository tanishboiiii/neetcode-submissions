class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        seq_poss = []

        # find possible sequence heads... (ie. only if i-1 doesn't exit in the arr)
        for i in nums:
            if (i-1) not in arr:
                seq_poss.append([i])

        # now you can try and build the sequences them selves...

        for seq in seq_poss:
            head = seq[0]
            flag = True
            while flag:
                head += 1
                if head not in arr:
                    flag = False
                else:
                    seq.append(head)
        
    

        longest = 0

        for seq in seq_poss:
            if len(seq) > longest:
                longest = len(seq)

        return longest