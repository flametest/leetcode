#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-22 13:04:09
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def comp_func(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0
        nums = map(str, nums)
        nums.sort(reverse=True, cmp=comp_func)
        result = "".join(nums).lstrip("0")
        return result if result else "0"






if __name__ == '__main__':
    print Solution().largestNumber([0])
    print Solution().largestNumber([3, 30, 34, 5, 9])