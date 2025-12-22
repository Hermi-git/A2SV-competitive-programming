class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        f = set(friends)
        for o in order:
            if o in f:
                ans.append(o)
        return ans