#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-03 09:50:26
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[:] = nums[length - k:] + nums[:length - k]

        # length = len(nums)
        # while k:
        #     tmp = nums[length - 1]
        #     for i in xrange(length - 1, 0, -1):
        #         nums[i] = nums[i - 1]
        #     nums[0] = tmp
        #     k -= 1

if __name__ == '__main__':
     s = Solution()
     print s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
     print s.rotate([1, 2], 1)
     print s.rotate([1], 0)
     print s.rotate([], 0)
