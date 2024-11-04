from unittest import TestCase
from io import StringIO
import sys

from main import parse_work_hours


class TestParseWorkHours(TestCase):
    """Класс UnitTest для функционала парсинга времени работника"""

    def test_empty_input(self) -> None:
        records = []

        expected_output = ""

        # Перенаправляем stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        parse_work_hours(records)

        # Возвращаем stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_single_worker(self) -> None:
        records = ["Иван 5", "Иван 8", "Иван 3"]

        expected_output = "Иван: 5, 8, 3; sum: 16\n"

        # Перенаправляем stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        parse_work_hours(records)

        # Возвращаем stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_many_workers(self) -> None:
        records = [
            "Андрей 9",
            "Василий 11",
            "Роман 7",
            "X Æ A-12 45",
            "Иван Петров 3",
            "Андрей 6",
            "Роман 11",
        ]

        expected_output = (
            "Андрей: 9, 6; sum: 15\n"
            "Василий: 11; sum: 11\n"
            "Роман: 7, 11; sum: 18\n"
            "X Æ A-12: 45; sum: 45\n"
            "Иван Петров: 3; sum: 3\n"
        )

        # Перенаправляем stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        parse_work_hours(records)

        # Возвращаем stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)
