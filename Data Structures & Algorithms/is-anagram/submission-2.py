class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {i:0 for i in s}
        t_count = {i:0 for i in t}

        for i in s:
            s_count[i] += 1
        
        for i in t:
            t_count[i] += 1

        if s_count == t_count:
            return True
        else:
            return False