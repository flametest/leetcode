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
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    print Solution().climbStairs(10)
