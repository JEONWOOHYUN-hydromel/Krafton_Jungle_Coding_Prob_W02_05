# 트리 - Implement Trie (Prefix Tree)
# 문제 링크: https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150
class Trie:

    def __init__(self):
        self.list_str = []

    def insert(self, word: str) -> None:
        self.list_str.append(word)

    def search(self, word: str) -> bool:
        for s in self.list_str:
            if s == word:
                return True
        return False
    def startsWith(self, prefix: str) -> bool:
        for s in self.list_str:
            if prefix in s:
                return True
        return False