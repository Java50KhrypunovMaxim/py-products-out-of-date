import unittest
from unittest.mock import patch, MagicMock
import datetime
from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
            {"name": "duck",
             "expiration_date": datetime.date(2022, 2, 1),
             "price": 160},
        ]

    @patch("app.main.datetime")
    def test_no_products_outdated(self, mock_datetime: MagicMock) -> None:
        mock_datetime.date.today.return_value = datetime.date(2022, 1, 30)
        self.assertEqual(outdated_products(self.products), [])

    @patch("app.main.datetime")
    def test_some_products_outdated(self, mock_datetime: MagicMock) -> None:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 6)
        self.assertEqual(outdated_products(self.products), ["chicken", "duck"])

    @patch("app.main.datetime")
    def test_all_products_outdated(self, mock_datetime: MagicMock) -> None:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 11)
        self.assertEqual(outdated_products(self.products),
                         ["salmon", "chicken", "duck"])
