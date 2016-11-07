#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-07 15:02:29
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(set(nums)) == 1:
                return 0
        nums.sort()
        return sum([i - nums[0] for i in nums])
            

if __name__ == '__main__':
    print Solution().minMoves([1])
    print Solution().minMoves([1, 1])
    print Solution().minMoves([1, 2])
    print Solution().minMoves([1, 2, 3])
    print Solution().minMoves([0, 3, 5])
    print Solution().minMoves([0, 1, 2, 3])
    print Solution().minMoves([-1, 2, 3])
    # print Solution().minMoves([1,2147483647])