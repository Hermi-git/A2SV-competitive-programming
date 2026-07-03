class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        summ = sum([int(num)for num in n_str])
        prod = 1
        for num in n_str:
            prod *= int(num)
        return prod - summ