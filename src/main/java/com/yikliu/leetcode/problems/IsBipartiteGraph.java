package com.yikliu.leetcode.problems;

import java.util.ArrayList;
import java.util.List;

/**
 * Given an undirected graph, return true if and only if it is bipartite.
 *
 * Recall that a graph is  bipartite  if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
 *
 * The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
 *
 * Example 1:
 * Input: [[1,3], [0,2], [1,3], [0,2]]
 * Output: true
 * Explanation:
 * The graph looks like this:
 * 0----1
 * |    |
 * |    |
 * 3----2
 * We can divide the vertices into two groups: {0, 2} and {1, 3}.
 *
 *
 *
 * Example 2:
 * Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
 * Output: false
 * Explanation:
 * The graph looks like this:
 * 0----1
 * | \  |
 * |  \ |
 * 3----2
 * We cannot find a way to divide the set of nodes into two independent subsets.
 *
 *
 *
 * Note:
 *
 *     graph will have length in range [1, 100].
 *     graph[i] will contain integers in range [0, graph.length - 1].
 *     graph[i] will not contain i or duplicate values.
 *     The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
 */
public class IsBipartiteGraph {

    /**
     * Initial a List<Int> colors with 0 size same as numbers of vertices.
     * paint 1 from point 0 and paint -1 with it's connected.
     * DO BFS until trying to paint a point with existing non-zero value. return false.
     * otherwise return true
     *
     * @param graph
     * @return
     */
    boolean isBipartite(int[][] graph) {
        List<Integer> colors = new ArrayList<>(graph.length);
        for (int i = 0; i < graph.length; i++) {
            if (colors.get(i) != 0 && !validate(i, 1, colors, graph )) {
                return false;
            }
        }
        return true;
    }

    boolean validate(int i, int expectedColor, List<Integer> colors, int[][] graphs) {
        if (colors.get(i) != 0)  {
            return colors.get(i) == expectedColor;
        }
        colors.set(i, expectedColor);
        for (int j = 0; j < graphs[i].length; j++) {
            if (!validate(graphs[i][j], -1 * expectedColor, colors, graphs)) {
                return false;
            }
        }
        return true;
    }
}
