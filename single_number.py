#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-26 12:30:34
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            d.setdefault(x, 0)
            d[x] += 1
        for k in d:
            if d[k] == 1:
                return k


if __name__ == '__main__':
    print Solution().singleNumber([1,2,2])
