class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]  
        self.is_end = False 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == ".":
                for child in node.children:
                    if child and dfs(child, i+1):
                        return True
                return False
            else:
                index = ord(ch) -ord("a")
                child = node.children[index]
                if child is None:
                    return False
                return dfs(child, i+1)

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)