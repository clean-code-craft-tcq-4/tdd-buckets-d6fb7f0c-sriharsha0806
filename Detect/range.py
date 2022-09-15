from typing import List
class Range:
    @staticmethod
    def range(readings: List[int]) -> List[str]:
        res = []
        readings = list(set(readings))
        readings.sort()
        start = end = 0
        while end < len(readings):
            while end+1 < len(readings) and readings[end]+1 == readings[end+1]:
                end = end+1
            if readings[start]!=readings[end]:
                res.append(f"{str(readings[start])}-{str(readings[end])}")
            else:
                res.append(str(readings[start]))
            end += 1
            start = end 
        return res 
        