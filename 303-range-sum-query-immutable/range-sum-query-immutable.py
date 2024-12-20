class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum = nums
        for i in range(1, len(nums)):
            self.prefixsum[i] += self.prefixsum[i-1] 
        print(self.prefixsum)
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefixsum[right] -self.prefixsum[left-1]
        else:
            return self.prefixsum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)