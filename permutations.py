#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 23:12:17
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        return self.helper([], nums, result)

    def helper(self, prev, curr, result=[]):
        if not curr:
            result.append(prev)
        for i, item in enumerate(curr):
            self.helper(prev + [item], curr[:i] + curr[i + 1:], result)
        return result


if __name__ == '__main__':
    # print Solution().helper([1, 2], [3, 4])
    print Solution().permute([])
    print Solution().permute([1, 2, 3])
