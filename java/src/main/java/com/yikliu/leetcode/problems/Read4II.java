package com.yikliu.leetcode.problems;

public class Read4II {
    private char[] buffer = new char[4];
    private int runner = 0;
    private int chaser = 0;

    public int read(char[] buf, int n) {
        for (int i = 0; i < n; i++) {
            if (runner == chaser) {
                runner = read4(buffer);
                chaser = 0;
                if(runner == 0) return i;
            }
            buf[i] = buffer[chaser++];
        }
        return n;
    }

    private int read4(char[] buf) {
        //for compiling only. OJ has implementation of this method.
        return 0;
    }
}
