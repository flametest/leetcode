#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-22 11:52:15
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        index = 1
        for i, item in enumerate(nums):
            if i < 1:
                continue
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
        return index


if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 2])
