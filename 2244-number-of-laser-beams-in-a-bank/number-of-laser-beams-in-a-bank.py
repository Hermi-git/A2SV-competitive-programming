class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = []
        for row in bank:
            if all(s == "0" for s in row):
                continue
            row = map(int, list(row))
            row_sum = sum(row)
            devices.append(row_sum)
        if len(devices) == 1:
            return 0
        laser = 0
        for i in range(len(devices)-1):
            laser += devices[i] * devices[i+1]
        return laser
