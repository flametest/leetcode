#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-19 22:38:16
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for num in nums:
            if nums[abs(num) - 1] < 0:
                return abs(num)
            else:
                nums[abs(num) - 1] = -nums[abs(num) - 1]


if __name__ == '__main__':
    print Solution().findDuplicate([1, 2, 3, 3, 3, 4])
    print Solution().findDuplicate([2, 1, 2])
    print Solution().findDuplicate([2, 2, 2, 2])
    print Solution().findDuplicate([3, 2, 2, 2, 4])
