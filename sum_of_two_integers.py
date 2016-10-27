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
        if a == 0:
            return b
        if b == 0:
            return a
        x = a ^ b #算出相加结果，不含进位
        y = a & b #算出进位
        z = y << 1 #移位相加
        return self.getSum(x, z)


if __name__ == '__main__':
    print Solution().getSum(1, 6)