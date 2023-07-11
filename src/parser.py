from src.parsers.numper_parser import NumberParser
from src.parsers.all_parser import AllParser
from src.parsers.separator_parser import SeparatorParser
from src.parsers.specific_parser import SpecificParser
from src.parsers.range_parser import RangeParser


class Parser:

    COMMA = ","
    HYPHEN = "-"
    ASTERISK = "*"
    SLASH = "/"

    @staticmethod
    def parse(val: str, _min: int, _max: int):
        values = []
        if val.isnumeric():
            res = [NumberParser.parse(_min, _max, int(val))]
        elif Parser.ASTERISK == val:
            res = AllParser.parse(_min, _max)
        elif Parser.SLASH in val:
            res = SeparatorParser.parse(_min, _max, val)
        elif Parser.COMMA in val:
            res = SpecificParser.parse(_min, _max, val)
        elif Parser.HYPHEN in val:
            res = RangeParser.parse(_min, _max, val)
        else:
            raise Exception(f"Invalid literal in the val: {val}")

        values.extend(res)
        return values
