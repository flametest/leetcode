#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-21 01:20:36
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def trailingZeroes_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        for i in range(1, n + 1):
            c += self.count_five(i)
        return c

    def count_five(self, n):
        c = 0
        while True:
            if n % 5 == 0:
                c += 1
            else:
                break
            n /= 5
        return c

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            c += n / 5
            n /= 5
        return c

    def factorial(self, n):
        if n == 1:
            return 1
        return self.factorial(n - 1) * n


if __name__ == '__main__':
    print Solution().trailingZeroes(1808548329)
    print Solution().trailingZeroes(100)
