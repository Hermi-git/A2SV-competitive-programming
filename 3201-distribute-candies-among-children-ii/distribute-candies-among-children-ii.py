class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def combination(x):
            if x < 0:
                return 0
            return ((x+1)* (x+2) )// 2
        
        all_comb = combination(n)
        one_child_above_limit = 3 * combination((n-(limit+1)))
        two_children_above_limit = 3 * combination((n - (2 *(limit+1))))
        all_children_above_limit = combination((n - (3 *(limit+1))))

        over_count = one_child_above_limit - two_children_above_limit + all_children_above_limit

        distribution = all_comb - over_count

        return distribution


    
