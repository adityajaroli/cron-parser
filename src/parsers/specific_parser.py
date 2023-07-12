from .numper_parser import NumberParser


class SpecificParser:
    @staticmethod
    def parse(_min, _max, val):
        temp = val.split(",")
        if not temp or len(temp) > 2 or not temp[0].isnumeric() or not temp[1].isnumeric():
            raise Exception(val)

        return [
            NumberParser.parse(_min, _max, temp[0]),
            NumberParser.parse(_min, _max, temp[1])
        ]
