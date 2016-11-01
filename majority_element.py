#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-01 12:36:06
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        no =[]
        for i in nums:
            if i in no:
                continue
            if nums.count(i) > len(nums) / 2:
                return i
            else:
                no.append(i)
        return -1

if __name__ == '__main__':
    print Solution().majorityElement([1,3,3,2,3])
