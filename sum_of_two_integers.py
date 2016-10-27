#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-26 14:35:40
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        MAX = 0x7FFFFFFF
        #MIN = 0x80000000
        MASK = 0xFFFFFFFF
        if a == 0:
            if b > MAX:
                return ~(b ^ MASK)
            else:
                return b
        if b == 0:
            if a > MAX:
                return ~(a ^ MASK)
            else:
                return a
        x = (a ^ b) & MASK#算出相加结果，不含进位
        y = (a & b) & MASK #算出进位
        z = (y << 1) & MASK #移位相加
        return self.getSum(x, z)


if __name__ == '__main__':
    print Solution().getSum(-1, 0)