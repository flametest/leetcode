#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-31 14:54:00
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, l in enumerate(reversed(list(s))):
            if i > 0:
                num += ((ALPHABET.index(l) + 1) * (26 ** i))
            else:
                num += (ALPHABET.index(l) + 1)
        return num

if __name__ == '__main__':
    # result 703
    print Solution().titleToNumber("A")
