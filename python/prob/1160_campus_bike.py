import heapq

class CampusBike:

    combos = []
    def buildup(self, dist, i, j):
        heapq.heappush(self.combos, (dist, i, j))

    def assignBikes(self, workers, bikes):
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                dist = abs(w[0] - b[0]) + abs(w[1] - b[1])
                self.buildup(dist, i, j)

        res = [-1 for _ in range(len(workers))]
        assignedbike = set()
        while self.comos:
            c, i, j = heapq.heappop(self.combos)
            if res[i] == -1 and j not in assignedbike:
                res[i] = j
                assignedbike.add(j)

        return res
