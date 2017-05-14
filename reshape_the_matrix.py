#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-14 12:04:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        result_nums = []
        if r < 0 or c < 0 or not nums:
            return nums
        o_r = len(nums)
        o_c = len(nums[0] if o_r else 0)
        if o_r * o_c != r * c:
            return nums
        new_row = []
        n = 0
        for i, row in enumerate(nums):
            for j, row_element in enumerate(row):
                print c, n, row_element
                if c >= n:
                    new_row.append(row_element)
                    n += 1
                else:
                    result_nums.append(new_row)
                    new_row = []
                    n = 0
        else:
            result_nums.append(new_row)

        return result_nums


if __name__ == '__main__':
    print Solution().matrixReshape([[1, 2], [3, 4]], 1, 4)
    print Solution().matrixReshape([[1, 2], [3, 4]], 2, 4)
    print Solution().matrixReshape([[1, 2], [3, 4]], -1, 4)
    print Solution().matrixReshape([[1, 2], [3, 4]], 1, -4)
    print Solution().matrixReshape([], 1, 4)
