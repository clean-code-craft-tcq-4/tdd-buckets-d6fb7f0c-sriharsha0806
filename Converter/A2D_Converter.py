class A2D_Converter:
    def __init__(self) -> None:
        self.min_bit = 0
        self.max_bit = 4094
        self.min_amp = 0
        self.max_amp = 10

    def map_value(self, bit_value):
        if bit_value > self.max_bit or bit_value < self.min_bit:
            return 'Error_reading, bit value not in range'
        return round(self.max_amp*bit_value/self.max_bit)

