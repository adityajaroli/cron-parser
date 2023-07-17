from .numper_parser import NumberParser
from src.fields.week_day_field import WeekDay

class RangeParser:

    @staticmethod
    def parse(field, val):
        temp = val.split("-")
        if not temp or len(temp) > 2:
            raise Exception(val)

        low = NumberParser.parse(field, temp[0])
        high = NumberParser.parse(field, temp[1])

        if low > high:
            raise Exception(val)

        return range(low, high + 1)
