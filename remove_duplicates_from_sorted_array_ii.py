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
            # The number at the end should be ignored.
            for j in range(i + 1, length - shift):
                if nums[j] == cur_num:
                    count += 1
                else:
                    break
            i += min(2, count)
            if count <= 2:
                continue
            # else shift the nums
            # the shift should be added up.
            shift = shift + count - 2
            for k in range(i, length - count + 2):
                nums[k] = nums[k + count - 2]
        print(nums)
        return len(nums) - shift


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        j = 2
        for i in range(2, n):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count += 1
                r += 1
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        print(nums)
        return l


if __name__ == '__main__':
    s = Solution()
    s1 = Solution1()
    s2 = Solution2()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(s.removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3]))
    print(s1.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(s1.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(s1.removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3]))
    print(s2.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(s2.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(s2.removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3]))
