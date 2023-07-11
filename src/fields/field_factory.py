from src.fields.minute_field import Minute
from src.fields.hour_field import Hour
from src.fields.month_day_field import MonthDay
from src.fields.month_field import Month
from src.fields.week_day_field import WeekDay


class FieldFactory:

    @staticmethod
    def get(filed_type):
        match filed_type:
            case "MIN":
                return Minute()
            case "HOUR":
                return Hour()
            case "DAY-OF-MONTH":
                return MonthDay()
            case "MONTH":
                return Month()
            case "DAY-OF-WEEK":
                return WeekDay()
            case _:
                return None

