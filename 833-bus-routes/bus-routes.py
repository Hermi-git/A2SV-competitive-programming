class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_buses = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus)
        starts = stop_to_buses[source]
        q = deque()
        visited = set()
        for start in starts:
            q.append((start, 1))
            visited.add(start)
        while q:
            bus, bus_count = q.popleft()
            for stop in routes[bus]:
                if stop  == target:
                    return bus_count
                for bus in stop_to_buses[stop]:
                    if bus not in visited:
                        q.append((bus, bus_count+1))
                        visited.add(bus)
        
        return -1
        

