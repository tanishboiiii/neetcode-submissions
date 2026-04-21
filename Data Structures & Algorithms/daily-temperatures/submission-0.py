class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = [] #(temp, index)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                cand_temp, j = stack.pop()
                res[j] = i-j

            stack.append((temp,i))
        
        return res