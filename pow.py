#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-18 16:59:24
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, n / 2)


if __name__ == '__main__':
    print Solution().myPow(0, 2)
    print Solution().myPow(3, 2)
    print Solution().myPow(0.00001, 2147483647)
