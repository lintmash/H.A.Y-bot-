import unittest
from unittest.mock import patch
from AM import get_date, submit, joke_of_the_day, query_complete
import datetime

class TestYourFunctions(unittest.TestCase):

    @patch('AM.datetime')
    def test_get_date(self, mock_datetime):
        mock_now = datetime.datetime(2023, 1, 1, 12, 0, 0)
        mock_datetime.now.return_value = mock_now

        result = get_date()

        self.assertEqual(result, ("01-Jan", "12:00"))

if __name__ == '__main__':
    unittest.main()
