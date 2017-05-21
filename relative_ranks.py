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
        sorted_nums = sorted(nums, reverse=True)
        for k, i in enumerate(sorted_nums):
            index = nums.index(i)
            if k == 0:
                nums[index] = "Gold Medal"
            elif k == 1:
                nums[index] = "Silver Medal"
            elif k == 2:
                nums[index] = "Bronze Medal"
            else:
                nums[index] = str(k + 1)
        return nums


if __name__ == '__main__':
    print Solution().findRelativeRanks([5, 4, 3, 2, 1])
    print Solution().findRelativeRanks([4, 3, 5, 2, 1])
    print Solution().findRelativeRanks([])
