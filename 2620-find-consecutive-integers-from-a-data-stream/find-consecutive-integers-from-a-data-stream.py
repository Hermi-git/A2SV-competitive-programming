class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        if len(self.queue) >= self.k:
            temp = self.queue.popleft()
            if temp == self.value:
                self.count -= 1
        self.queue.append(num)
        if self.value == num:
            self.count += 1
        
        return self.count == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)