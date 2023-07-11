class NumberParser:

    @staticmethod
    def parse(_min, _max, val):
        parsed_val = int(val)
        if _min <= parsed_val <= _max:
            return parsed_val
        else:
            raise Exception(val)
