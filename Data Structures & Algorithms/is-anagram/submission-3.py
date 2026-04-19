class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {i:0 for i in s}
        t_count = {i:0 for i in t}

        for char in s:
            s_count[char] += 1

        for char in t:
            t_count[char] += 1

        if s_count == t_count:
            return True
        
        return False

