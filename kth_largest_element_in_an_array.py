#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-26 23:38:35
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-2]


if __name__ == '__main__':
    print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
