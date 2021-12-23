package com.yikliu.leetcode.problems;

import java.util.AbstractMap;
import java.util.Comparator;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
 *
 * (Here, the distance between two points on a plane is the Euclidean distance.)
 *
 * You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
 *
 *
 *
 * Example 1:
 *
 * Input: points = [[1,3],[-2,2]], K = 1
 * Output: [[-2,2]]
 * Explanation:
 * The distance between (1, 3) and the origin is sqrt(10).
 * The distance between (-2, 2) and the origin is sqrt(8).
 * Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
 * We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
 *
 * Example 2:
 *
 * Input: points = [[3,3],[5,-1],[-2,4]], K = 2
 * Output: [[3,3],[-2,4]]
 * (The answer [[-2,4],[3,3]] would also be accepted.)
 */
public class KClosestPoints {
    public int[][] kClosest(int[][] points, int K) {
        int[][] ans = new int[K][2];
        double dist = 0;
        PriorityQueue<Map.Entry<Double, Integer>> included = new PriorityQueue<>(K, new Comparator<Map.Entry<Double, Integer>>() {
            @Override public int compare(Map.Entry<Double, Integer> o1, Map.Entry<Double, Integer> o2) {
                if (o1.getKey() < o2.getKey()) {
                    return -1;
                } else {
                    return 1;
                }
            }
        });
        Map.Entry<Double, Integer> top;
        for (int i = 0; i < points.length; i++) {
            dist = getDistance(points[i]);
            if (included.size() < K) {
                included.add(new AbstractMap.SimpleEntry<Double, Integer>(dist, i));
            } else {
                top = included.peek();
                if (top.getKey() > dist) {
                    included.poll();
                    included.add(new AbstractMap.SimpleEntry<>(dist, i));
                }
            }
        }

        for (int t = 0; t < K; t++) {
            ans[t] = points[included.poll().getValue()];
        }
        return ans;
    }

    private double getDistance(int[] point) {
        return Math.sqrt(Math.pow(point[0], 2) + Math.pow(point[1], 2));
    }
}
