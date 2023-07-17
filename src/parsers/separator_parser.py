from .numper_parser import NumberParser
from ..fields.week_day_field import WeekDay


class SeparatorParser:
    @staticmethod
    def parse(field, val):
        result = []
        temp = val.split("/")

        if not temp or len(temp) > 2:
            raise Exception(val)

        delta = NumberParser.parse(field, temp[1])

        # Either * or a number
        if temp[0] == "*":
            start_from = 0
        else:
            start_from = NumberParser.parse(field, temp[0])

        _, _max = field.get_min_max()

        while start_from <= _max:
            result.append(start_from)
            start_from += delta

        return result
