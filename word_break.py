#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-14 17:16:56
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for w in wordDict:
                if dp[i - len(w)] and s[(i - len(w)): i] == w:
                    dp[i] = True
        return dp[-1]
            

if __name__ == '__main__':
    print Solution().wordBreak("leetcode", ["leet", "code"])
