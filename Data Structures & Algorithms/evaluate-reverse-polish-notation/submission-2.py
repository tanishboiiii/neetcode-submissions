class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        [3]
        
        for i in tokens:
            if i in "+-*/":
                val2 = int(stack.pop())
                val1 = int(stack.pop())

                if i == "+":
                    stack.append(val1+val2)
                elif i == "-":
                    stack.append(val1-val2)
                elif i == "/":
                    stack.append(val1/val2)
                else:
                    stack.append(val1*val2)
            else:
                stack.append(int(i))

        return int(stack.pop())

        