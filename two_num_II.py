#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 11:23:16
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, i in enumerate(numbers):
            for index2, j in enumerate(numbers[index1:]):
                if i + j == target and i != j:
                    return [index1 + 1, index2 + 1]


if __name__ == '__main__':
    print Solution().twoSum([2, 7, 11, 15], 9)
    print Solution().twoSum([1, 2, 3, 4], 4)
