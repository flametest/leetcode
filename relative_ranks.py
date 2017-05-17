#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 10:40:34
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums = sorted(nums, reverse=True)
        nums[0] = "Gold Medal"
        nums[1] = "Silver Medal"
        nums[2] = "Bronze Medal"
        return nums


if __name__ == '__main__':
    print Solution().findRelativeRanks([5, 4, 3, 2, 1])
