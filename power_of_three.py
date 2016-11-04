#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-04 18:18:23
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n:
            if n == 1:
                break
            if n % 3 == 0:
                n = n / 3
            else:
                return False
        return True



if __name__ == '__main__':
    print Solution().isPowerOfThree(1)
    print Solution().isPowerOfThree(3)
    print Solution().isPowerOfThree(-3)
    print Solution().isPowerOfThree(0)
