import heapq


class CompareStringsFreqSmallestChar:

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def freq(word):
            f = [0 for _ in range(26)]
            for i in word:
                f[ord(i) - ord('a')] += 1
            for n in f:
                if n > 0:
                    return n
            return 0

        heap = []
        for w in words:
            heapq.heappush(heap, (freq(w), -1, w))
        for i, q in enumerate(queries):
            heapq.heappush(heap, (freq(q), i, q))

        res = [0 for _ in range(len(queries))]
        w_count = 0
        while heap:
            f, index, w = heapq.heappop(heap)
            if index == -1:
                w_count += 1
            else:
                res[index] = len(words) - w_count
        return res

