class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def Trie():
            return defaultdict(Trie)
        
        sent = sentence.split(" ")
        trie = Trie()
        def insert(trie, word):
            node = trie
            for ch in word:
                node = node[ch]
            node["end"] = True

        for word in dictionary:
            insert(trie, word)

        def search_root(trie, word):
            node = trie
            prefix = ""
            for ch in word:
                if ch not in node:
                    break
                node = node[ch]
                prefix += ch
                if "end" in node: 
                    return prefix
            return word  

        replaced_word = [search_root(trie, w) for w in sent]
        return " ".join(replaced_word)
                