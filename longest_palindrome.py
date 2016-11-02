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




if __name__ == '__main__':
    print Solution().longestPalindrome("abccccdd")
    print Solution().longestPalindrome("")
    print Solution().longestPalindrome("ccc")
    print Solution().longestPalindrome("bcccaaaaadd")
    print Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
    # print Solution().longestSub(["c", "c", "c", "a", "a", "a", "a", "a" ])