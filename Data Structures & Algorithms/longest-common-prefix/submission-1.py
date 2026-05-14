class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
  
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
            

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        node = trie.root
        for word in strs: trie.insert(word)
        prefix = ""
        while len(node.children) == 1 and not node.is_end:
            prefix += list(node.children.keys())[0]
            node = node.children[list(node.children.keys())[0]]
        return prefix
        