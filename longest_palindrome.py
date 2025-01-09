#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-01 14:30:27
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        other = []
        double = []
        single = []
        for l in s:
            if s.count(l) % 2 == 0:
                double.append(l)
            elif s.count(l) % 2 != 0 and s.count(l) != 1:
                other.append(l)
            else:
                single.append(l)
        if other:
            return len(double) + self.longestSub(other)
        elif single:
            return len(double) + 1
        else:
            return len(double)

    def longestSub(self, t):
        d = {}
        for i in t:
            if i in d:
                d[i] += 1
            else:
                d[i] = 0

        return len(t) - len(d.keys()) + 1


class Solution1:
    def longestPalindrome(self, s: str) -> int:
        count = dict()
        res = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2
        for v in count.values():
            if v % 2 == 1:
                res += 1
                break
        return res


if __name__ == '__main__':
    print(Solution1().longestPalindrome("abccccdd"))
    print(Solution1().longestPalindrome(""))
    print(Solution1().longestPalindrome("ccc"))
    print(Solution1().longestPalindrome("bcccaaaaadd"))
    print(Solution1().longestPalindrome(
        "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
    # print Solution().longestSub(["c", "c", "c", "a", "a", "a", "a", "a" ])
