class IntegerToRoman:
    def __init__(self):
        self.values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        self.symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

    def convert(self, num):
        roman = ""
        i = 0

        while num > 0:
            while num >= self.values[i]:
                roman += self.symbols[i]
                num -= self.values[i]
            i += 1

        return roman


# Example usage
converter = IntegerToRoman()
print(converter.convert(1))     # I
print(converter.convert(4))     # IV
print(converter.convert(9))     # IX
print(converter.convert(58))    # LVIII
print(converter.convert(1994))  # MCMXCIV
