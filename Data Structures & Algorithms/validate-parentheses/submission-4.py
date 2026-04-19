class Solution:
    def isValid(self, s: str) -> bool:
        check = {"}": "{", ")": "(", "]": "["}  
        stack = []  
  
        for i in s:  
            if i in check.values():  
                stack.append(i)  
            else:  
                if not stack:  
                    return False  
                  
                open_bracket = stack.pop()  
                if check[i] != open_bracket:  
                    return False  
      
        return not stack  