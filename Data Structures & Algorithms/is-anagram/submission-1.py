class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s_freq = {}
        t_freq = {}

        for i in range(len(s)):
            if s[i] in s_freq:
                s_freq[s[i]] += 1
            else:
                s_freq[s[i]] = 0

            if t[i] in t_freq:
                t_freq[t[i]] += 1
            else:
                t_freq[t[i]] = 0
        
        return s_freq == t_freq