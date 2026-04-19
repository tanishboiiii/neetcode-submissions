class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {num:0 for num in nums}
        freq = {i:[] for i in range(1, len(nums)+1)}

        for num in nums:
            count[num] += 1
        
        for num in count:
            freq[count[num]].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
