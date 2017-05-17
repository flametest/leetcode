#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 09:04:27
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$
# silmiar question:     521 Longest Uncommon Subsequence I


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one_num_list = []
        n = 0
        one_num_list.append(n)
        for i in nums:
            if i == 1:
                n += 1
            else:
                one_num_list.append(n)
                n = 0
        else:
            one_num_list.append(n)
        return max(one_num_list)


if __name__ == '__main__':
    print Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
    print Solution().findMaxConsecutiveOnes([1, 1, 0])
    print Solution().findMaxConsecutiveOnes([0, 1, 1])
    print Solution().findMaxConsecutiveOnes([0])
    print Solution().findMaxConsecutiveOnes([1])
    print Solution().findMaxConsecutiveOnes([])
