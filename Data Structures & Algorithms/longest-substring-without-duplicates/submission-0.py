class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window_start = 0
        char_active = set()

        for window_end in range(0, len(s)):            
            while s[window_end] in char_active:
                # remove the character duplicate?
                char_active.remove(s[window_start])
                window_start += 1
            
            char_active.add(s[window_end])
            max_length = max(max_length, window_end - window_start + 1)




        return max_length