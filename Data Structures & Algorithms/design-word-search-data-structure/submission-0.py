class TrieNode:
    def __init__(self, is_leaf: bool = False):
        self.children = {}
        self.is_leaf = is_leaf

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_leaf = True

    def dfs(self, word: str, node: TrieNode):
        if len(word) == 0:
            return node.is_leaf

        char = word[0]

        if char in node.children and char != '.':
            return self.dfs(word[1:], node.children[char])

        if char not in node.children and char != '.':
            return False

        isWord = False

        for child in node.children:
            isWord += self.dfs(word[1:], node.children[child])

        return True if isWord > 0 else False

    def search(self, word: str):
        return self.dfs(word, self.root)
        # node = self.root
        # for char in word:
        #     if char not in node.children and char != '.':
        #         return False
        #     if char != '.': 
        #         node = node.children[char]
        #     else:
        #         node = node.children[]

        # return node.is_leaf


class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        
    def addWord(self, word: str) -> None:
        self.trie.addWord(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)
        
