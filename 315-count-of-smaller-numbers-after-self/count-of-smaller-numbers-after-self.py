class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums_store = []
        for i, num in enumerate(nums):
            nums_store.append((num,i))
        counts = [0]*len(nums)
        right_small_count = 0
        def merge(left, right):
            nonlocal right_small_count 
            l = 0
            r = 0
            merged_arr=[]
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged_arr.append(left[l])
                    idx = left[l][1]
                    counts[idx] += r
                    l += 1
                else:
                    merged_arr.append(right[r])
                    r += 1
            while l < len(left):
                idx = left[l][1]
                counts[idx] += r 
                merged_arr.append(left[l])
                l += 1
            while r < len(right):
                merged_arr.append(right[r])
                r += 1
            return merged_arr
        def mergeSort(l, r, arr):
            if l == r:
                return [(arr[l][0], arr[l][1])]
            mid = (l+r)//2
            left_arr = mergeSort(l, mid, arr)
            right_arr = mergeSort(mid+1, r, arr)

            return merge(left_arr, right_arr)
        mergeSort(0, len(nums)-1, nums_store)
        return counts
        