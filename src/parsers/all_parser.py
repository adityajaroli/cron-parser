class AllParser:

    @staticmethod
    def parse(field):
        _min, _max = field.get_min_max()
        return range(_min, _max + 1)
