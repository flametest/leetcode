#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-13 19:22:30
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childnodes = []
        self.char = ""
        self.is_word = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.insert_helper(word, self)

    def insert_helper(self, word, node):
        if not word:
            node.is_word = True
            return
        for n in node.childnodes:
            if word[0] == n.char:
                self.insert_helper(word[1:], n)
                break
        else:
            new_node = Trie()
            new_node.char = word[0]
            node.childnodes.append(new_node)
            self.insert_helper(word[1:], new_node)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.search_helper(word, self)

    def search_helper(self, word, node):
        if not word and node.is_word:
            return True
        elif not word and not node.is_word:
            return False
        for n in node.childnodes:
            if word[0] == n.char and self.search_helper(word[1:], n):
                return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.startsWith_helper(prefix, self)

    def startsWith_helper(self, word, node):
        if not word:
            return True
        elif not word and not node.is_word:
            return False
        for n in node.childnodes:
            if word[0] == n.char and self.startsWith_helper(word[1:], n):
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("abc")
# obj.insert("abd")
# print obj
# print obj.search("abc")
# print obj.search("ab")
# print obj.search("bd")
# print obj.startsWith("ab")
# print obj.startsWith("b")
obj = Trie()
obj.insert("ab")
print obj.search("a")
print obj.startsWith("a")
