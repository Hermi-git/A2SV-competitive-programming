class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        stack = []
        for i in range(len(p)):
            if p[i] == "" or p[i] == ".":
                continue
            elif p[i] == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p[i])
        return "/" + "/".join(stack)