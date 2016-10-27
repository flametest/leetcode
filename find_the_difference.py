#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-27 19:43:46
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = list(t)
        for x in list(s):
            if x in l:
                l.remove(x)
        return l.pop()

if __name__ == '__main__':
    print Solution().findTheDifference("abcd", "abcde")
    print Solution().findTheDifference("aa", "aaa")
