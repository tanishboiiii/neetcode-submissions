class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            encoding = [0]*26
            for c in s:
                encoding[ord(c) - ord("a")] += 1
        
            result[tuple(encoding)].append(s)
        
        return result.values()