#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-01-07 22:42:41
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/remove-element
# @Version : $Id$
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        count = len(nums)
        while i <= j:
            if nums[j] == val:
                j -= 1
                count -= 1
                continue
            if nums[i] == val:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                count -= 1
                j -= 1
            i += 1

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([1], 1))
    print(s.removeElement([3, 2, 2, 3], 3))
    print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
