class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            print(stack)
            if op.isnumeric() or len(op) > 1 and op[0] == "-":
                stack.append(op)
            elif op == "C":
                if stack:
                    stack.pop()
            elif op == "D":
                stack.append(2 * int(stack[-1]))
            elif op == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
        answer = sum(int(num) for num in stack)
        return answer
        
            
