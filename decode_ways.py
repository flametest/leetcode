#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 14:42:40
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 0
        if "1" <= s[0] <= "9":
            dp[1] = 1
        else:
            dp[1] = 0
        for i in range(2, length + 1):
            one = s[i-1:i]
            two = s[i-2:i]
            if "1" <= one <= "9":
                dp[i] += dp[i - 1]
            if "10" <= two <= "26":
                if i - 2 == 0:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[length]


if __name__ == '__main__':
    s = Solution()
    print s.numDecodings("")
    print s.numDecodings("12")
    print s.numDecodings("012")
    print s.numDecodings("123")
