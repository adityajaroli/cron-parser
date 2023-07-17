from .numper_parser import NumberParser


class SpecificParser:
    @staticmethod
    def parse(field, val):
        temp = val.split(",")
        if not temp:
            raise Exception(val)

        return [NumberParser.parse(field, el) for el in temp]
