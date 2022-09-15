import unittest 
from Detect.range import Range
from Detect.reading import Reading
from Detect.csv_formatter import Csv_formatter
from Converter.A2D_Converter import A2D_Converter
from Converter.error_handling import error_handling

class TypewiseTest(unittest.TestCase):    
    def test_find_range(self):
        samples = [3,3,5,4,10,11,12]
        samples_II = [3,3,5,4,10]
        self.assertTrue(Range.range(samples)==['3-5', '10-12'])     
        self.assertTrue(Range.range(samples_II)==['3-5', '10'])

    def test_reading(self):
        samples = [3,3,5,4,10,11,12]
        samples_II = [3,3,5,4,10]
        self.assertTrue(Reading.reading(samples, ['3-5', '10-12'])=={'3-5':4, '10-12':3})
        self.assertTrue(Reading.reading(samples_II, ['3-5', '10'])=={'3-5':4, '10':1}) 

    def test_csv_output(self):
        self.assertTrue(Csv_formatter.csv_format({'3-5':4, '10-12':3}) == "Range, Readings"+'\n'+"3-5, 4"+'\n'+"10-12, 3")
        self.assertTrue(Csv_formatter.csv_format({'3-5':4, '10':1}) == "Range, Readings"+'\n'+"3-5, 4"+'\n'+"10, 1")

    def test_error_handling(self):
        A2D_convert = A2D_Converter()
        self.assertTrue(error_handling.error_handling(A2D_convert.map_value(4094))=="All is Well!")
        self.assertTrue(error_handling.error_handling(A2D_convert.map_value(1028))=="All is Well!")
        #self.assertTrue(error_handling.error_handling(A2D_convert.map_value(4095))=="ValueError: Work with Positive Integers Only")

if __name__ == '__main__':
    unittest.main()