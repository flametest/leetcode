#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-06 10:16:09
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        total = m + n
        index1 = index2 = 0
        for i in range(m, m+n):
            nums1[i] = float("inf")
        while nums2 and index1 < total and index2 < n:
            if nums1[index1] >= nums2[index2]:
                self.readjust(index1, nums1, total)
                nums1[index1] = nums2[index2]
                index1 += 1
                index2 += 1
            else:
                index1 += 1
        print nums1

    def readjust(self, index, nums1, total):
        i = total - 1
        while i > index:
            nums1[i] = nums1[i - 1]
            i -= 1


if __name__ == '__main__':
    s = Solution()
    # print s.merge([1, 3, 5, 0, 0, 0], 3, [2, 4, 6] , 3)
    # # print s.readjust(0, [1, 3, 5, 0, 0, 0], 6)
    # print s.merge([2, 4, 6, 0, 0, 0], 3, [1, 3, 5], 3)
    # print s.merge([8, 9, 10, 0, 0, 0], 3, [1, 3, 5], 3)
    # print s.merge([0], 0, [1], 1)
    print s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
