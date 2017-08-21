#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-21 16:39:59
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        st = {}
        for i in nums:
            if i in st:
                st[i] += 1
            else:
                st[i] = 0
        return sorted(st.keys(), key=lambda x: st[x], reverse=True)[:k]


if __name__ == '__main__':
    print Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print Solution().topKFrequent([3, 0, 1, 0], 1)
