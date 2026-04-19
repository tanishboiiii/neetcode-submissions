class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"{":"}", "(":")", "[":"]"}
        track = []
        
        for i in s:
            if i in bracket_map:
                track.append(i)
            else:
                if len(track) == 0:
                    return False

                brack = track.pop()

                if bracket_map[brack] != i:
                    return False

        if len(track) == 0:
            return True
        else:
            return False    
    