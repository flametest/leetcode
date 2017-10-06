#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-06 10:16:10
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        result = 0
        positive = not ((dividend > 0) ^ (divisor > 0))
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            tmp = divisor
            count = 1
            while dividend >= tmp:
                tmp <<= 1
                count <<= 1
            result += count >> 1
            dividend -= tmp >> 1
        if not positive:
            result = -result
        if result > MAX_INT:
            return MAX_INT
        elif result < MIN_INT:
            return MIN_INT
        else:
            return result


if __name__ == '__main__':
    s = Solution()
    print s.divide(10, 3)
