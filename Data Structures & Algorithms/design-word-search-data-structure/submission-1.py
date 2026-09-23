class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(i: int, node: TrieNode):
            if i == len(word):
                return node.end

            ch = word[i]
            
            if ch == '.':
                return any(dfs(i + 1, child) for child in node.children.values())
            
            if ch not in node.children:
                return False

            return dfs(i + 1, node.children[ch])
        return dfs(0, self.root)