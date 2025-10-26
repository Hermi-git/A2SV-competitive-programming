class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            p = succProb[i]
            graph[u].append((v, p))
            graph[v].append((u, p))

        def dijkstra(start, end):
            if start_node == end_node:
                return 1.0

            probability = [0.0 for node in range(n)]
            probability[start] = 1.0

            heap = [(-1.0, start)]
            while heap:
                neg_prob, node = heapq.heappop(heap)
                pos_prob = -(neg_prob)
                for child, prob in graph[node]:
                    new_prob = pos_prob * prob
                    if new_prob > probability[child]:
                        probability[child] = new_prob
                        heapq.heappush(heap, (-(new_prob), child))
            print(probability)
            return probability[end]
        
        return dijkstra(start_node, end_node)
