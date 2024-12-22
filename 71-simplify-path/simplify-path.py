class Solution:
    def simplifyPath(self, path: str) -> str:
        stack =[]
        for dire in path.split('/'):
            if dire == "." or dire == "":
                continue
            elif dire == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dire)
        return '/' + '/'.join(stack)