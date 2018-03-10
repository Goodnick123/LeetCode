# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 12:28
# @Author  : Yeh
import collections
class TrieNode(object):
    def __init__(self):
        self.exist=False
        self.children = collections.defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root =TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current =self.root
        for letter in word:
            current =current.children[letter]
        current.exist=True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current =self.root
        for letter in word:
            current =current.children.get(letter)
            if current is None:
                return False
        return current.exist

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current =self.root
        for letter in prefix:
            current =current.children.get(letter)
            if current is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
word ='nick'
prefix= 'ni'
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
print(param_2)
print(param_3)