package com.yikliu.leetcode.problems;

import java.util.Map;
import java.util.HashMap;

public class SubArrayEqualToK {
	public int solve(int[] nums, int k) {
		int sum = 0;
		int res = 0;
		Map<Integer, Integer> m = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {
			sum += nums[i];
			res += m.get(sum - k);
			m.merge(sum, 1, Integer::sum);
		}
		return res;
	}
}
