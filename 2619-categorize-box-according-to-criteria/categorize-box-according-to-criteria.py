class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        vol = length * width * height

        if (max(length, width, height) >= 10**4 or vol >= 10**9) and (mass >= 100):
            return 'Both'
        elif max(length, width, height) >= 10**4 or vol >= 10**9:
            return 'Bulky'
        elif  mass >= 100:
            return 'Heavy'
        else:
            return 'Neither'
    
 