#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-14 14:15:17
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # length = len(s)
        # result = 0
        # for j in range(length + 1):
        #     matrix = [0 for _ in range(length + 1)]
        #     tmp = []
        #     for i  in range(j, length + 1):
        #         if i == 0:
        #             matrix[i] == 0
        #         elif s[i - 1] not in tmp:
        #             matrix[i] = matrix[i - 1] + 1
        #             tmp.append(s[i - 1])
        #             result = max(matrix[i], result)
        #         else:
        #             matrix[i] = 1
        #             tmp = []
        #             tmp.append(s[i - 1])
        # return result

        result = 0
        tmp = {}
        left = 0
        for i, n in enumerate(s):
            if n in tmp and left <= tmp[n]:
                left = tmp[n] + 1
            else:
                result = max(result, i - left + 1)
            tmp[n] = i
        return result


if __name__ == '__main__':
    # print Solution().lengthOfLongestSubstring("")
    # print Solution().lengthOfLongestSubstring("c")
    # print Solution().lengthOfLongestSubstring("abcabcbb")
    # print Solution().lengthOfLongestSubstring("bbbbb")
    print Solution().lengthOfLongestSubstring("pwwkew")
    print Solution().lengthOfLongestSubstring("dvdf")
    print Solution().lengthOfLongestSubstring("ibuwnuxdaudvevtbyntmduprwuvuvnbdrvcepzjswmnckidivxubrjspdplacmetkizbjktfzihjrltoknpdyhsdyf")
