#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-18 21:55:13
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    print Solution().climbStairs(4)
