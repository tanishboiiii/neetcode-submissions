class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums: # O(n)
            freq[num] += 1
        
        buckets = defaultdict(list) 

        for i in freq:
            buckets[freq[i]].append(i)
        
        ans = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        