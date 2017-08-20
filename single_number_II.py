#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-20 10:01:54
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return (sum([i * 3 for i in set(nums)]) - sum(nums)) / 2


if __name__ == '__main__':
    print Solution().singleNumber([4, 4, 4, 3, 3, 3, 2])
    print Solution().singleNumber([0, 0, 0, 5])
