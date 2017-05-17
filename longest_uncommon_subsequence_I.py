#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 18:28:53
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$
# silmiar question: 485. Max Consecutive Ones


class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        max_num = 0
        for i in a:
            n = 0
            for j in b:
                if i != j:
                    n += 1
                else:
                    if n > max_num:
                        max_num = n
                    break
            else:
                max_num = n
        return max_num


if __name__ == '__main__':
    print Solution().findLUSlength("aba", "cdc")
    print Solution().findLUSlength("", "cdc")
    print Solution().findLUSlength("abcd", "cdc")
    print Solution().findLUSlength("abcd", "bcd")
