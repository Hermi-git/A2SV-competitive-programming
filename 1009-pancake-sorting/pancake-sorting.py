class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, k):
            arr[:k] = arr[:k][::-1]
        
        def find_max(arr, n):
            max_index = 0
            for i in range(n):
                if arr[i] > arr[max_index]:
                    max_index = i
            return max_index
        
        result = []
        for i in range(len(arr), 1, -1):
            max_index = find_max(arr, i)

            
            if max_index != i-1:
                if max_index != 0:
                    result.append(max_index+1)
                    flip(arr, max_index+1)
                result.append(i)
                flip(arr, i)

        return result