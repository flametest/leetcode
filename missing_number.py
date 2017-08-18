#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-18 21:02:18
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sn = n * (n + 1) / 2
        return sn - sum(nums)


if __name__ == '__main__':
    print Solution().missingNumber([0, 1, 3])
    print Solution().missingNumber([0, 2, 3])
