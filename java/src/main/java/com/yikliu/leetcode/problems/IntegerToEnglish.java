package com.yikliu.leetcode.problems;

/**
 * Input: num = 123
 * Output: "One Hundred Twenty Three"
 */
public class IntegerToEnglish {
	public String solve(int num) {
		String[] w = new String[]{"Thousand", "Million", "Billion"};
		String res = hundred(num % 1000);
		int i = 0;
		String trail = "";
		while(num / 1000 > 0) {
			num /= 1000;
		    trail = res.equals("") ? "" : " ";
			res = hundred(num % 1000) + " " + w[i] +  trail + res;
			i++;
		}
		return res.isEmpty() ? "Zero" : res;
	}

	private String hundred(int num) {
		String res = "";
		String[] underTwenty = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
		String[] tenties = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

		int h = num / 100;
		int t = num % 100;
		int o = num % 10;

		if (h > 0) {
			res += underTwenty[h] + " Hundred";
		}

		String header = h == 0 ? "" : " ";
		if (t >= 20) {
			res += header + tenties[t / 10] + (o > 0 ? " " + underTwenty[o] : "");
		} else {
			res += (t > 0 ? header + underTwenty[t] : "");
		}

		return res;
	}
}
