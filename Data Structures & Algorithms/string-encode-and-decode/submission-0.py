class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for i in strs:
            code += (str(len(i)) + "$" + i)
        return code

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while (i < len(s)):
            j = i
            while (s[j] != "$"):
                j+=1
            
            length = int(s[i:j])
            i = j+1
            string = s[i:i+length]
            ans.append(string)
            i += length

        return ans
