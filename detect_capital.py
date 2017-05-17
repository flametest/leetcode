#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 09:47:24
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$



class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        import re
        pattern = re.compile(r"^[a-z]+$|^[A-Z]+$|^[A-Z][a-z]+$")
        if re.match(pattern, word):
            return True
        else:
            return False


if __name__ == '__main__':
    print Solution().detectCapitalUse("GooGle")
    print Solution().detectCapitalUse("Google")
    print Solution().detectCapitalUse("google")
    print Solution().detectCapitalUse("USA")
    print Solution().detectCapitalUse("U")
    print Solution().detectCapitalUse("a")
    print Solution().detectCapitalUse("googlE")
    print Solution().detectCapitalUse("GOogle")
