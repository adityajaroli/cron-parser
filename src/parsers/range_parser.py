from .numper_parser import NumberParser


class RangeParser:

    @staticmethod
    def parse(_min, _max, val):
        temp = val.split("-")
        if not temp or len(temp) > 2 or not temp[0].isnumeric() or not temp[1].isnumeric():
            raise Exception(val)

        low = NumberParser.parse(_min, _max, int(temp[0]))
        high = NumberParser.parse(_min, _max, int(temp[1]))

        if low > high:
            raise Exception(val)

        return range(low, high + 1)