from .numper_parser import NumberParser


class RangeParser:

    @staticmethod
    def parse(_min, _max, val):
        temp = val.split("-")
        if not temp or len(temp) > 2:
            raise Exception(val)

        low = NumberParser.parse(_min, _max, temp[0])
        high = NumberParser.parse(_min, _max, temp[1])

        if low > high:
            raise Exception(val)

        return range(low, high + 1)
