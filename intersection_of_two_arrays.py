#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-28 15:19:50
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        return list(set(nums1)&set(nums2))



if __name__ == '__main__':
    print Solution().intersection([1,22,3], [2,2])
