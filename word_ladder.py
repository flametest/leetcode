#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-22 16:08:09
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord not in wordList:
            wordList.append(beginWord)
        visited = {}
        adjacent = self.compose_graph(wordList)
        gen_result = list(self.helper(beginWord, endWord, wordList, adjacent, visited))
        if not gen_result:
            return 0
        distance = min(map(len, gen_result))
        return distance
    
    def helper(self, beginWord, endWord, wordList, adjacent, visited):
        visited[beginWord] = 0
        if beginWord == endWord:
            yield [beginWord]
        for adj_word in adjacent[beginWord]:
            if adj_word not in visited:
                for i in self.helper(adj_word, endWord, wordList, adjacent, visited):
                    yield [beginWord] + i
        # delete the word as we need to find other solution during the entire process
        visited.pop(beginWord)

    def compose_graph(self, wordList):
        adjacent = {}
        for word in wordList:
            nearby = self.find_one_diff(word, wordList)
            adjacent[word] = nearby
        return adjacent

    def find_one_diff(self, word, wordList):
        result = []
        for w in wordList:
            diff = 0
            for x, y in zip(list(w), list(word)):
                if x != y:
                    diff += 1
            if diff == 1:
                result.append(w)
        return result


if __name__ == '__main__':
    print Solution().ladderLength(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"]
    )
    print Solution().ladderLength(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log"]
    )
    print Solution().ladderLength(
        "hot",
        "dog",
        ["hot", "dog", "dot"]
    )
    # print Solution().ladderLength(
    #     "qa",
    #     "sq",
    #     ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    # )
    # print Solution().find_one_diff("hot", ["hot", "dot", "dog", "lot", "log", "cog"])
