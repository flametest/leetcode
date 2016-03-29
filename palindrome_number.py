#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-29 15:28:15
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        return x == int("".join(reversed(list(str(x)))))



if __name__ == '__main__':
    a = 1331
    print Solution().isPalindrome(a)
