class NumberParser:

    @staticmethod
    def parse(_min, _max, val: str):

        if not val.isnumeric():
            raise Exception(f"Value should have been a numeric. {val}")

        parsed_val = int(val)
        if _min <= parsed_val <= _max:
            return parsed_val
        else:
            raise Exception(val)
