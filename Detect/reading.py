from typing import List, Dict 

class Reading:
    @staticmethod 
    def reading(samples: List[int], intervals: List[str])->Dict[str, int]:
        d = {}
        for sample in samples:
            for interval in intervals:
                if interval not in d:
                    d[interval] = 0
                if len(interval.split('-')) == 2:
                    ll, ul = interval.split('-')
                    ll, ul = int(ll), int(ul)
                    if sample in range(ll, ul+1):
                        d[interval] += 1
                else:
                    if sample == int(interval):
                        d[interval] += 1
        return d
