class MinStack:

    def __init__(self):
        self.stack = []
        self.minsSoFar = []

        self.minimum = float("inf")
        self.minPrev = None
        

    def push(self, val: int) -> None:
        if val <= self.minimum:
            self.minsSoFar.append(self.minPrev)
            self.minPrev = self.minimum
            self.minimum = val

        self.stack.append(val)


    def pop(self) -> None:
        top_val = self.top()

        if top_val == self.minimum:
            self.minimum = self.minPrev
            self.minPrev = self.minsSoFar.pop()
        
        self.stack.pop()
        
        return top_val

        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
        
