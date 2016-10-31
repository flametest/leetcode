#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-31 14:35:54
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for letter in list(magazine):
            d.setdefault(letter, 0)
            d[letter] += 1

        for l in list(ransomNote):
            if l not in magazine:
                return False
            if d[l] < ransomNote.count(l):
                return False
        return True


if __name__ == '__main__':
    print Solution().canConstruct("a", "b")
    print Solution().canConstruct("a", "a")
    print Solution().canConstruct("aa", "ab")
    print Solution().canConstruct("aa", "aab")
