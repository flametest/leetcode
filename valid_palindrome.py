#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 14:27:18
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        find_str = re.findall(r"[A-Za-z\d]*", s)
        find_str = [l for l in find_str if l]
        extract_str = "".join(find_str)
        extract_str = extract_str.lower()
        return extract_str == extract_str[::-1]


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome("")
    print s.isPalindrome("A man, a plan, a canal: Panama")
    print s.isPalindrome("race a car")
    print s.isPalindrome("0P")
