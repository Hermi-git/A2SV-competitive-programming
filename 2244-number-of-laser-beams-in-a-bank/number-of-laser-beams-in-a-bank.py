class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laser = 0
        devices = []
        for row in bank:
            if all(s == "0" for s in row):
                continue
            row = map(int, list(row))
            row_sum = sum(row)
            devices.append(row_sum)
        if len(devices) == 1:
            return 0
        res = 0
        for i in range(len(devices)-1):
            res += devices[i] * devices[i+1]
        return res
