package com.yikliu.leetcode.problems;

public class IntegerToEnglish {
	public String solve(int num) {
		String[] w = new String[]{"Thousand", "Million", "Billion"};
		String res = hundred(num % 1000);
		int i = 0;
		while(num / 1000 > 0) {
			num /= 1000;
			res = hundred(num % 1000) + " " + w[i] + res;
			i++;
		}
		return res.isEmpty() ? "Zero" : res;
	}

	private String hundred(int num) {
		String res = "";
		String[] underTwenty = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twleve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
		String[] Tenties = {"", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

		int h = num / 100;
		int t = num % 100; 
		int o = num % 10;

		if (h > 0) {
			res += underTwenty[h] + " Hundred";
		}
		if (t > 20) {
			res += " " + Tenties[t / 10] + (o > 0 ? " " + underTwenty[o] : "");
		} else {
			res += (t > 0 ? " " + underTwenty[t] : "");
		}

		return res;
	}
}
