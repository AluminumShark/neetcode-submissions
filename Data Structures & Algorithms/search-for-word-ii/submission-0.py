class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w
        
        R, C = len(board), len(board[0])
        res = []

        def dfs(r: int, c: int, node: TrieNode):
            ch = board[r][c]
            if ch not in node.children:
                return
            
            nxt = node.children[ch]

            if nxt.word is not None:
                res.append(nxt.word)
                nxt.word = None
            
            board[r][c] = '#'

            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, nxt)
            if r < R - 1 and board[r + 1] != '#':
                dfs(r + 1, c, nxt)
            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, nxt)
            if c < C - 1 and board[r][c + 1] != '#':
                dfs(r, c + 1, nxt)

            board[r][c] = ch

            if not nxt.children:
                node.children.pop(ch, None)

        for r in range(R):
            for c in range(C):
                dfs(r, c, root)
        
        return res







