#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-14 09:13:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split(" ")
        result_list = []
        for word in word_list:
            result_list.append(word[::-1])
        return " ".join(result_list)


if __name__ == '__main__':
    print Solution().reverseWords("Let's take LeetCode contest")
    print Solution().reverseWords("")
    print Solution().reverseWords("Let's")
