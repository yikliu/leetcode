package com.yikliu.leetcode.problems;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

/**
 * Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
 */
public class RemoveInvalidParentheses {
	public List<String> solve(String s) {
		Queue<String> q = new LinkedList<>();
		Set<String> visited = new HashSet<>();
		List<String> res = new ArrayList<>();
		q.add(s);
		boolean found = false;
		while(!q.isEmpty()) {
			String s1 = q.poll();
			if (isValid(s1)) {
				res.add(s1);
				found = true;
			}
			if (found) continue;
			for (int i = 0; i < s1.length(); i++) {
				if (s1.charAt(i) != '(' && s1.charAt(i) != ')') continue;
				String s2 = s1.substring(0, i) + s1.substring(i + 1);
				if (visited.add(s2)) {
					q.offer(s2);
				}
			}
		}
		return res;
	}

	private Boolean isValid(String s) {
		int cnt = 0;
		for (char c : s.toCharArray()) {
			if (c == '(') cnt++;
			if (c == ')') cnt--;
			if (cnt < 0) return false;
		}
		return cnt == 0;
	}
}
