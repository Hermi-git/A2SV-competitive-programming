class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()  
        answer = []
        
        for query in queries:  
            summ = 0
            count = 0
            for num in nums: 
                if summ + num <= query:
                    summ += num
                    count += 1
                else:
                    break 
            answer.append(count)  
        
        return answer


