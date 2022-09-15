from Detect.range import Range
from Detect.reading import Reading
from Detect.csv_formatter import Csv_formatter

def print_on_console(message):
    print(message)

def range(samples):
    intervals = Range.range(samples)
    d = Reading.reading(samples, intervals)
    msg = Csv_formatter.csv_format(d)
    print_on_console(msg)


if __name__ == '__main__':
    range([3,3,4,5,10,11,12])
