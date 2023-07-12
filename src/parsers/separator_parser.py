from .numper_parser import NumberParser


class SeparatorParser:
    @staticmethod
    def parse(_min, _max, val):
        result = []
        temp = val.split("/")

        if not temp or len(temp) > 2:
            raise Exception(val)

        delta = NumberParser.parse(_min, _max, temp[1])

        # Either * or a number
        if temp[0] == "*":
            start_from = 0
        else:
            start_from = NumberParser.parse(_min, _max, temp[0])

        while start_from <= _max:
            result.append(start_from)
            start_from += delta

        return result
