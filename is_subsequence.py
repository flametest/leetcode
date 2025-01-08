#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-01-08 18:36:01
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/is-subsequence
# @Version : $Id$


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) != 0 and len(t) == 0:
            return False
        i1 = i2 = 0
        while True:
            if s[i1] != t[i2]:
                i2 += 1
            elif s[i1] == t[i2]:
                i1 += 1
                i2 += 1
            if i1 > len(s) - 1:
                return True
            if i1 <= len(s) - 1 and i2 > len(t) - 1:
                return False


class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == len(s)


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
    print(s.isSubsequence("axc", "ahbgdc"))
    print(s.isSubsequence("", "ahbgdc"))
