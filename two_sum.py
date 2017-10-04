#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-04 12:15:39
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if not nums:
            return result

        for i, num in enumerate(nums):
            other = target - num
            if other in nums:
                index = nums.index(other)
                if index == i:
                    continue
                else:
                    result.append(i)
                    result.append(index)
                break
        return result


if __name__ == '__main__':
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9)
    print s.twoSum([3, 2, 4], 6)
    print s.twoSum([3, 3], 6)
