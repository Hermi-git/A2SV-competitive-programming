class Solution:
    def minOperations(self, logs: List[str]) -> int:
        log_stack = []
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if log_stack:
                    log_stack.pop()
            else:
                log_stack.append(log)
        return len(log_stack)
                
