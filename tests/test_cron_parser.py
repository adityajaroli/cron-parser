import unittest
import pytest
from src.cron_parser import CronParser
from .happy_path_expressions import happy_path_expressions
from .corner_case_expressions import corner_cases_expressions


class TestCronParser(unittest.TestCase):

    parser = CronParser()

    def test_cron_parser_when_expression_is_null(self):
        with pytest.raises(Exception) as e:
            self.parser.parse(cron_expression=None)
        assert str(e.value) == 'The expression cannot be empty or null!'

    def test_cron_parser_when_expression_is_empty(self):
        with pytest.raises(Exception) as e:
            self.parser.parse(cron_expression="")
        assert str(e.value) == 'The expression cannot be empty or null!'

    def test_validate_happy_path(self):
        for expression, expected in happy_path_expressions.items():
            actual = self.parser.parse(expression)
            assert actual == expected, f"Actual: {actual} and Expected: {expected}"

    def test_validate_corner_cases(self):
        for expression in corner_cases_expressions:
            with pytest.raises(Exception):
                self.parser.parse(expression)
