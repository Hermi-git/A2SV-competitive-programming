class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        arr1_count = defaultdict(int)
        last_elt= []
        for n in arr1:
            if n not in arr2_set:
                last_elt.append(n)
            arr1_count[n] += 1
        last_elt.sort()

        result = []
        for n in arr2:
            for _ in range(arr1_count[n]):
                result.append(n)
        
        return result + last_elt

