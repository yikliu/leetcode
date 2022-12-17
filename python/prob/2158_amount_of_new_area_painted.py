'''
'''


import collections
import heapq


class Solution(object):
    def amountPainted(self, paint):
        """
        :type paint: List[List[int]]
        :rtype: List[int]
        """
        points = collections.defaultdict(list)
        for i, (s, e) in enumerate(paint):
            points[s].append((True, i))
            points[e].append((False, i))
        min_heap = []
        lookup = [False]*len(paint)
        result = [0]*len(paint)
        prev = -1
        for pos in sorted(points.iterkeys()):
            while min_heap and lookup[min_heap[0]]:
                heapq.heappop(min_heap)
            if min_heap:
                result[min_heap[0]] += pos-prev
            prev = pos
            for t, i in points[pos]:
                if t:
                    heapq.heappush(min_heap, i)
                else:
                    lookup[i] = True
        return result
