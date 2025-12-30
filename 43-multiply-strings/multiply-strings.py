class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1, res2 = 0, 0
        for i in num1:
            res1 = res1 * 10 + (ord(i) - ord("0")) 
        for i in num2:
            res2 = res2 * 10 + (ord(i) - ord("0")) 

        return str(res1 * res2)
        