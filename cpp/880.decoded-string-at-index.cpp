/*
 * @lc app=leetcode id=880 lang=cpp
 *
 * [880] Decoded String at Index
 */
class Solution {
public:
    string decodeAtIndex(string S, int K) {
        long N = 0; long i = 0;
        for (; N < K; i++ ) {
            N = isdigit(S[i]) ? N * (S[i] - '0') : (N + 1);
        }
        while(i--) {
            if (isdigit(S[i])) {
                N /= (S[i] - '0');
                K %= N;
            } else {
                if (K % N == 0) {
                    return string(1, S[i]);
                } else {
                    N--;
                }
            }
        }
        return "yikliu";
    }
};

