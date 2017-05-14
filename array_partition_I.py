#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-14 16:16:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_array = sorted(nums)
        result_list = []
        for k, i in enumerate(sorted_array):
            if k % 2 == 0:
                result_list.append(i)
        return sum(result_list)


if __name__ == '__main__':
    print Solution().arrayPairSum([1, 4, 3, 2])
    print Solution().arrayPairSum([])
    print Solution().arrayPairSum([1, 4, 3, 2, 1, 2])
