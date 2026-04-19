class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string = [] # acts like a stack
        result = []

        def backtracking(openN, closeN):
            if openN == closeN == n:
                result.append("".join(string))
                return

            if openN < n:
                string.append("(")
                backtracking(openN+1, closeN)
                string.pop()
            
            if closeN < openN:
                string.append(")")
                backtracking(openN, closeN+1)
                string.pop()
        
        backtracking(0, 0)
        return result