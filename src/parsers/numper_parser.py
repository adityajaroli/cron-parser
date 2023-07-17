class NumberParser:

    @staticmethod
    def parse(field, val: str):

        if not val.isnumeric():
            raise Exception(f"Value should have been a numeric. {val}")
        _min, _max = field.get_min_max()

        parsed_val = int(val)
        if _min <= parsed_val <= _max:
            return parsed_val
        else:
            raise Exception(val)
