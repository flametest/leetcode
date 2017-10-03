#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-03 09:42:50
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        word_dict = {}
        for word in strs:
            char_list = list(word)
            key = "".join(sorted(char_list))
            word_dict.setdefault(key, []).append(word)
        return word_dict.values()



if __name__ == '__main__':
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print s.groupAnagrams(None)
