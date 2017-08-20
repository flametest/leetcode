#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-20 23:40:12
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            if n & 0x01 == 1:
                c += 1
            n >>= 1
        return c


if __name__ == '__main__':
    print Solution().hammingWeight(1)
    print Solution().hammingWeight(11)
    print Solution().hammingWeight(0)
