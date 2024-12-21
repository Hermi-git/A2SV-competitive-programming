class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        summ = 0
        prefix_dict = {0 : 1}

        for num in nums:
            summ += num

            if summ - k in prefix_dict:
                count += prefix_dict[summ - k]
            
            prefix_dict[summ] = prefix_dict.get(summ, 0) + 1
        return count
        
