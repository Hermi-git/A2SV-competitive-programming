class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def sorted_list(to_sort, order):
            return sorted(to_sort, key=lambda x: position[x])

        graph = defaultdict(list)
        indegree = [0] * n
        for i in range(n):
            for j in range(len(beforeItems[i])):
                graph[beforeItems[i][j]].append(i)
                indegree[i] += 1
        group_dict = defaultdict(list)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            group_dict[group[i]].append(i)
      
        q = deque()
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        if len(order) < n:
            return []

        position = [0] * n
        for i, node in enumerate(order):
            position[node] = i
        group_dep = defaultdict(set)
        group_indegree = [0] * (max(group_dict.keys())+1)
        for v in range(n):
            for u in beforeItems[v]:
                group_u = group[u]
                group_v = group[v]

                if group_u != group_v:
                    if group_v not in group_dep[group_u]:
                        group_dep[group_u].add(group_v)
                        group_indegree[group_v] += 1
        group_order = []
        group_q = deque()
        for i in range(len(group_indegree)):
            if group_indegree[i] == 0:
                group_q.append(i) 
        while group_q:
            group = group_q.popleft()
            group_order.append(group)
            for neigh in group_dep[group]:
                group_indegree[neigh] -= 1
                if group_indegree[neigh] == 0:
                    group_q.append(neigh)
        if len(group_order) < len(group_dict):
            return []
        answer = []
        for group in group_order:
            items = sorted_list(group_dict[group], order)
            answer.extend(items)
        for group in group_dict:
            if group not in group_order:
                items = sorted_list(group_dict[group], order)
                answer.extend(items)
        return answer 
        


        