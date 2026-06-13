import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0

        graph = {}

        for u, v, t in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, t))

        heap = [(0, k)]

        visited = set()
        res = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            res = time

            if node in graph:
                for nei, cost in graph[node]:
                    if nei not in visited:
                        heapq.heappush(heap, (time + cost, nei))

        if len(visited) == n:
            return res
        else:
            return -1