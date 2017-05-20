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
        nums = sorted(nums)
        for k, i in enumerate(nums):
            if k == 0:
                nums[k] = "Gold Medal"
            elif k == 1:
                nums[k] = "Silver Medal"
            elif k == 2:
                nums[k] = "Bronze Medal"
            else:
                nums[k] = k + 1
        return nums


if __name__ == '__main__':
    print Solution().findRelativeRanks([5, 4, 3, 2, 1])
