#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-28 15:05:51
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for x in nums:
            if x == 0:
                pass
            else:
                nums[i] = x
                i += 1
        for j in range(1, len(nums) - i + 1):
            nums[-j] = 0


if __name__ == '__main__':
    nums = [1, 0, 2 ,0, 0, 0, 3, 0, 12]
    Solution().moveZeroes(nums)
    print nums
