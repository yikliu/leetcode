'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from typing import Collection
import unittest
import collections


def ladder_length(begin_word, end_word, word_list):
    """
    :type begin_word: str
    :type end_word: str
    :type word_list: List[str]
    :rtype: int
    """
    d = set(word_list)
    q = collections.deque()
    v = set()

    q.append((begin_word, 1))
    v.add(begin_word)

    while q:
        pair = q.popleft()

        if pair[0] == end_word:
            return pair[1]

        word, cost = pair
        temp = list(word)

        for i in range(len(word)):
            for j in range(26):
                temp[i] = chr(ord("a") + j)
                temp = "".join(temp)

                if temp in d and temp not in v:
                    v.add(temp)
                    q.append((temp, cost + 1))

                temp = list(temp)
                temp[i] = word[i]

    return 0

class TestWordLadder(unittest.TestCase):
    def test_1(self):
        res = ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        self.assertEqual(res, 5)

    def test2(self):
        res = ladder_length(
            "qa",
            "sq",
            [
                "si",
                "go",
                "se",
                "cm",
                "so",
                "ph",
                "mt",
                "db",
                "mb",
                "sb",
                "kr",
                "ln",
                "tm",
                "le",
                "av",
                "sm",
                "ar",
                "ci",
                "ca",
                "br",
                "ti",
                "ba",
                "to",
                "ra",
                "fa",
                "yo",
                "ow",
                "sn",
                "ya",
                "cr",
                "po",
                "fe",
                "ho",
                "ma",
                "re",
                "or",
                "rn",
                "au",
                "ur",
                "rh",
                "sr",
                "tc",
                "lt",
                "lo",
                "as",
                "fr",
                "nb",
                "yb",
                "if",
                "pb",
                "ge",
                "th",
                "pm",
                "rb",
                "sh",
                "co",
                "ga",
                "li",
                "ha",
                "hz",
                "no",
                "bi",
                "di",
                "hi",
                "qa",
                "pi",
                "os",
                "uh",
                "wm",
                "an",
                "me",
                "mo",
                "na",
                "la",
                "st",
                "er",
                "sc",
                "ne",
                "mn",
                "mi",
                "am",
                "ex",
                "pt",
                "io",
                "be",
                "fm",
                "ta",
                "tb",
                "ni",
                "mr",
                "pa",
                "he",
                "lr",
                "sq",
                "ye",
            ],
        )
        self.assertEqual(res, 5)

