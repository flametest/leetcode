#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-06 15:09:56
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        return self.helper("", n, n, result)
        
    def helper(self, s, l, r, result):
        if l:
            self.helper(s + "(", l - 1, r, result)
        if r > l:
            self.helper(s + ")", l, r - 1, result)
        if not r:
            result.append(s)
        return result

        
if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(2))
