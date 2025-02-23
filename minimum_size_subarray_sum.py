#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-01-16 22:22:40
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/minimum-size-subarray-sum
# @Version : $Id$
from typing import List


# this solution exceed the time limit.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = 1
        n = len(nums)
        while length <= n:
            for i in range(n - length + 1):
                subarray = nums[i:i + length]
                if sum(subarray) >= target:
                    return length
            length += 1
        return 0


class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = total = 0
        res = float('inf')
        for r, item in enumerate(nums):
            total += item
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
        return res if res < float('inf') else 0


if __name__ == '__main__':
    s = Solution1()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
    print(s.minSubArrayLen(4, [1, 4, 4]))  # 1
    print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0
    print(s.minSubArrayLen(15, [1, 2, 3, 4, 5]))  # 5
