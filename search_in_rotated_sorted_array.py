#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-03 10:24:37
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        length = len(nums)
        k = 1
        rotated = False
        for i in xrange(1, length):
            if nums[i] < nums[i - 1]:
                rotated = True
                break
            k += 1
        nums = nums[k:] + nums[:k]
        low, high = 0, length - 1
        while low < high:
            mid = (low + high) / 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                # 因为python里mid除法是向下取整，所以这里高位不减一
                high = mid
            else:
                index = mid
                break
        else:
            index = low if target == nums[low] else -1
        real_index = -1
        if index == -1:
            return index
        if rotated:
            real_index = index + k
        else:
            real_index = index
        return real_index if real_index < length else real_index - length


if __name__ == '__main__':
    s = Solution()
    print s.search([], 2) # -1
    print s.search([4, 5, 6, 7, 0, 1, 2], 2) # 6
    print s.search([0, 1, 2, 4, 5, 6, 7], 3) # -1
    print s.search([1, 3, 5], 3) # 1
    print s.search([3, 5, 1], 3) # 0
    print s.search([3, 5, 1], 5) # 1
    print s.search([5, 1, 3], 5) # 0
    print s.search([3, 1], 1) # 1
    print s.search([3, 1], -1) # -1
    print s.search([3, 1], 3) # 0
