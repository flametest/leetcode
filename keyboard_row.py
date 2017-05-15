#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 17:50:44
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
                    ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
                    ["z", "x", "c", "v", "b", "n", "m"]]

        result = []
        for word in words:
            n = 0
            word_list = []
            for w in word:
                lw = w.lower()
                if lw in keyboard[0]:
                    n = 0
                if lw in keyboard[1]:
                    n = 1
                if lw in keyboard[2]:
                    n = 2
                word_list.append(n)
            if len(set(word_list)) == 1:
                result.append(word)
        return result


if __name__ == '__main__':
    print Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
