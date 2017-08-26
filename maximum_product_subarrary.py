#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-26 21:07:11
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mid_max = mid_min = max_val = nums[0]
        for num in nums[1:]:
            temp = [num, mid_min * num, mid_max * num]
            mid_max = max(temp)
            mid_min = min(temp)
            max_val = max(max_val, mid_max)
        return max_val
            


if __name__ == '__main__':
    print Solution().maxProduct([])
    print Solution().maxProduct([-2])
    print Solution().maxProduct([-2, 3])
    print Solution().maxProduct([2, 3, -2, 4])
