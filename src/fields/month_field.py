class Month:

    MONTH_MAP = {
        "JAN": "1",
        "FEB": "2",
        "MAR": "3",
        "APR": "4",
        "MAY": "5",
        "JUN": "6",
        "JUL": "7",
        "AUG": "8",
        "SEP": "9",
        "OCT": "10",
        "NOV": "11",
        "DEC": "12"
    }

    @staticmethod
    def get_min_max():
        return 1, 12

    def map_it_to_number(self, val):
        for key, value in self.MONTH_MAP.items():
            if key in val:
                val = val.replace(key, value)
        return val
