from math import floor
class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) == float:
            return cls(floor(float_value))
        return 'value is not a float'

    @classmethod
    def from_roman(cls, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in roman:
                num += roman[s[i:i+2]]
                i += 2
            else:
                # print(i)
                num += roman[s[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_string(cls, str_value):
        if type(str_value) == str:
            return cls(int(str_value))
        return 'wrong type'


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
