#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-04 18:02:47
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = bin(n)
        if x.count("1") == 1 and n > 0:
            return True
        return False


if __name__ == '__main__':
    print Solution().isPowerOfTwo(1)
    print Solution().isPowerOfTwo(24)
    print Solution().isPowerOfTwo(8)
