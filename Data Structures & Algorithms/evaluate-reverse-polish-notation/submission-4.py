class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for i in range(len(tokens)):
            
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                if tokens[i] == operators[0]:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a) + int(b))
                elif tokens[i] == operators[1]:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b) - int(a))
                elif tokens[i] == operators[2]:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(a) * int(b))
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(int(b) / int(a)))

        return int(stack[0])

