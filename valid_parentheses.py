#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-21 00:01:41
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        a = []
        for i in s:
            if i in m.keys():
                a.append(i)
            elif i in m.values():
                if a and m[a[-1]] == i:
                    a.pop()
                else:
                    return False
        if a:
            return False
        return True


if __name__ == '__main__':
    # print Solution().isValid("[23(xx{xxx})]")
    # print Solution().isValid("[23(xx{xxx))]")
    print Solution().isValid("]")
