class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == "[":
                stack.append(i)
            elif i == "{":
                stack.append(i)
            elif i == ")" and len(stack) > 0:
                if stack[len(stack) - 1] == "(":
                    stack.pop()
                else:
                    return False
            elif i == "]" and len(stack) > 0:
                if stack[len(stack) - 1] == "[":
                    stack.pop()
                else:
                    return False

            elif i == "}" and len(stack) > 0:
                if stack[len(stack) - 1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False