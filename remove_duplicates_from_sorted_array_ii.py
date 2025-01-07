#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-01-07 23:28:41
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
# @Version : $Id$
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        shift = 0
        while i < length - 1:
            count = 1
            cur_num = nums[i]
            for j in range(i + 1, length - shift):
                if nums[j] == cur_num:
                    count += 1
                else:
                    break
            i += min(2, count)
            if count <= 2:
                continue
            # else shift the nums
            shift = shift + count - 2
            for k in range(i, length - count + 2):
                nums[k] = nums[k + count - 2]
        print(nums)
        return len(nums) - shift


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(s.removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3]))
