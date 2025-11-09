class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def Trie():
            return defaultdict(Trie)
        
        sent = sentence.split(" ")
        trie = Trie()
        def insert(trie, word):
            curr = trie
            for ch in word:
                curr = curr[ch]
            curr["end"] = True

        for word in dictionary:
            insert(trie, word)

        def search_root(trie, word):
            curr = trie
            prefix = ""
            for ch in word:
                if ch not in curr:
                    break
                curr = curr[ch]
                prefix += ch
                if "end" in curr: 
                    return prefix
            return word  

        replaced_word = [search_root(trie, w) for w in sent]
        return " ".join(replaced_word)
                