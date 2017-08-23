#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 03:15:14
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_mapping = {
            "1" : ["*"],
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
            "0" : [" "]
        }
        result = []
        trans_list = []
        for i in digits:
            if i in letter_mapping:
                trans_list.append(letter_mapping[i])
            else:
                raise ValueError
        result = []
        for k, l in enumerate(trans_list):
            if k == 0:
                result = l
            if k + 1 == len(trans_list):
                break
            result = self.combination(result, trans_list[k + 1])
        return result

    def combination(self, prev_l, curr_l):
        result = []
        for i in prev_l:
            for j in curr_l:
                result.append(i + j)
        return result


if __name__ == '__main__':
    print Solution().combination(["a", "b", "c"], ["d", "e", "f"])
    print Solution().letterCombinations("223")
