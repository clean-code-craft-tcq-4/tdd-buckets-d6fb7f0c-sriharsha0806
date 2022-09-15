class Csv_formatter:
    @staticmethod
    def csv_format(d):
        res = []
        ans = ""
        res.append(f"Range, Readings")
        for range, freq in d.items():
            res.append(f"{range}, {freq}")
        ans = "\n".join(res)
        return ans 