#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 13:50:55
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        max_num = max(nums)
        min_num = min(nums)
        x = range(min_num, max_num + 1)
        result = list(set(x) - set(nums))
        return result


if __name__ == '__main__':
    print Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
