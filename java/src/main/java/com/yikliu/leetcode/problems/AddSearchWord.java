package com.yikliu.leetcode.problems;

import java.util.ArrayList;
import java.util.List;

/**
 * Design a data structure that supports the following two operations:
 *
 * void addWord(word)
 * bool search(word)
 *
 * search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
 *
 * For example:
 *
 * addWord("bad")
 * addWord("dad")
 * addWord("mad")
 * search("pad") -> false
 * search("bad") -> true
 * search(".ad") -> true
 * search("b..") -> true
 *
 * Note:
 * You may assume that all words are consist of lowercase letters a-z
 */
public class AddSearchWord {
    class TreeNode {
        List<TreeNode> children = new ArrayList<>(26);
        boolean isWord;
    }

    private TreeNode root;

    public AddSearchWord() {
        root = new TreeNode();
    }

    public void addWord(final String word) {
        int v = -1;
        TreeNode p = root;
        for (int i = 0; i < word.length(); i++) {
            v = word.charAt(i) - 'a';
            if (p.children.get(v) == null) {
                p.children.set(v, new TreeNode());
            }
            if (i == word.length() - 1) {
                p.children.get(v).isWord = true;
            }
            p = p.children.get(v);
        }
    }

    public boolean searchWord(String pattern, TreeNode n) {
        TreeNode p = n;
        int v = -1;
        for (int i = 0; i < pattern.length(); i++ ) {
            if (pattern.charAt(i) == '.') {
                return searchWord(pattern.substring(i + 1), p);
            }
            v = pattern.charAt(i) - 'a';
            if (p.children.get(v) != null) {
                if (p.children.get(v).isWord) {
                    return true;
                }
                p = p.children.get(v);
            }else {
                return false;
            }
        }
        return false;
    }

    public boolean searchWord(String pattern) {
        return searchWord(pattern, root);
    }
}
