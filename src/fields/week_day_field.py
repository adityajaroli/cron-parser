class WeekDay:

    WEEK_DAY_MAPPING = {
        "MON": "1",
        "TUE": "2",
        "WED": "3",
        "THU": "4",
        "FRI": "5",
        "SAT": "6",
        "SUN": "7",
    }

    @staticmethod
    def get_min_max():
        return 1, 7

    # val = "MON,TUE"
    def map_it_to_number(self, val):
        for key, value in self.WEEK_DAY_MAPPING.items():
            if key in val:
                val = val.replace(key, value)
        return val
