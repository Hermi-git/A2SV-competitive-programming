class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]  
        self.is_end = False 
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for ch in key:
            index = ord(ch) - ord('a') 
            if curr.children[index] is None:
                curr.children[index]=TrieNode()
            curr = curr.children[index]
        curr.is_end = True
        curr.value = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for ch in prefix:
            index = ord(ch) - ord('a') 
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]
        @cache
        def dfs(node):
            nonlocal result
            if not node:
                return 0
            if node.is_end:
                result= node.value
            else:
                result=0
            
            for child in node.children:
                result += dfs(child)
            return result

        result = 0
        return dfs(curr)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)