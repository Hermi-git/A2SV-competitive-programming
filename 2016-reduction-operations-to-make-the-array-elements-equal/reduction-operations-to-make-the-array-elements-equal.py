class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique= sorted(count.keys(), reverse=True)
        total = len(nums)
        operation = 0
        for i in range(len(unique)-1):
            largest = unique[i]
            next_largest =unique[i+1]
            largest_count = count[largest]
            operation += largest_count
            count[next_largest] += largest_count
            
        return operation 