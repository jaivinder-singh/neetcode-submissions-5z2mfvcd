class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in ("+", "-", "*", "/"):
                stack.append(int(tok))
            else:
                second = stack.pop()
                first = stack.pop()
                operation = tok
                if operation == "+":
                    total = first + second
                elif operation == "-":
                    total = first - second
                elif operation == "*":
                    total = first * second
                else:
                    total = int(first / second)

                stack.append(total)
        
        return stack[0]