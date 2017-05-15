#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 17:21:43
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result_list = []
        for i in findNums:
            index = nums.index(i)
            for j in range(index, len(nums)):
                if nums[j] > i:
                    result_list.append(nums[j])
                    break
            else:
                result_list.append(-1)
        return result_list


if __name__ == '__main__':
    print Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
    print Solution().nextGreaterElement([2, 4], [1, 2, 3, 4])
