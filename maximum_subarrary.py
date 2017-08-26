#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-26 23:18:16
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_val = curr_max = nums[0]
        for num in nums[1:]:
            # 1. include num or 2. num only 
            curr_max = max(curr_max + num, num)
            # or 3. nothing to do with num
            max_val = max(max_val, curr_max)
        return max_val


if __name__ == '__main__':
    print Solution().maxSubArray([])
    print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
