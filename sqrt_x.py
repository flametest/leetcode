#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-05 15:51:44
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return x
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if x < mid * mid:
                r = mid
            elif mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            else:
                l = mid + 1



if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(6))
