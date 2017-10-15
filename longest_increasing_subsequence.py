#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-14 12:18:11
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        dp = [0] * length
        for i in range(length):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)



if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
