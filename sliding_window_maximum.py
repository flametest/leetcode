#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-10 17:29:01
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = []
        result = []
        for i, num in enumerate(nums):
            while deque and nums[deque[-1]] < num:
                deque.pop()
            deque.append(i)
            if i >= k - 1:
                result.append(nums[deque[0]])
            if deque[0] <= i - k + 1:
                deque.pop(0)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)