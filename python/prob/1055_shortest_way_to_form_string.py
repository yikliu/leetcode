class ShortestWayToFormString:

    def shortest_way(self, source, target):
        i, j, m, n = 0, 0, len(source), len(target)

        res = 0

        while j < n:
            pre = j

            for i, c in enumerate(source):
                if i < m and c == target[j]:
                    j += 1
            if j == pre:
                return -1
            res += 1
        return res

