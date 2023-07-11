from src.fields.field_factory import FieldFactory
from src.parser import Parser


class CronParser:

    TIME_FIELDS = ["MIN", "HOUR", "DAY-OF-MONTH", "MONTH", "DAY-OF-WEEK", "COMMAND"]

    @staticmethod
    def __validate(cron_expression):
        if not cron_expression:
            raise Exception("The expression cannot be empty or null!")
        if len(cron_expression.split(" ")) != 6:
            raise Exception(f"The expression should have exact 6 sections. {CronParser.TIME_FIELDS}")

    def parse(self, cron_expression):
        try:
            self.__validate(cron_expression)

            store = {}
            sections = cron_expression.split(" ")

            for i in range(len(sections)):
                field = self.TIME_FIELDS[i]
                values = self.__parse_field(field, sections[i])
                store[field] = values
            return store
        except Exception as e:
            raise e

    @staticmethod
    def __parse_field(field, _input):
        field_obj = FieldFactory.get(field)
        # This means field is "command"
        if not field_obj:
            return _input
        _min, _max = field_obj.get_min_max()
        return Parser.parse(_input, _min, _max)
