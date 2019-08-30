import unittest
from task import TubeStations as ts



class Cases(unittest.TestCase):

    def test_case_1(self):
        """Anywhere in Zone 1 £2.50 From Holborn to Aldgate."""
        tubestations = ts()
        self.assertEqual(tubestations.balance('Holborn', 'Aldgate'), 2.5)

    def test_case_2(self):
        """Any one zone outside zone 1 £2.00 From Arsenal to Hammersmith."""
        tubestations = ts()
        self.assertEqual(tubestations.balance('Arsenal', 'Hammersmith'), 2.00)

    def test_case_3(self):
        """Any two zones including zone 1 £3.00 From Hammersmith to Holborn."""
        tubestations = ts()
        self.assertEqual(tubestations.balance('Hammersmith', 'Holborn'), 3.00)

    def test_case_4(self):
        """Any two zones excluding zone 1 £2.25 From Arsenal to Wimbledon."""
        tubestations = ts()
        self.assertEqual(tubestations.balance('Arsenal', 'Wimbledon'), 2.25)

    def test_case_5(self):
        """More than two zones (3+) £3.20 From Wimbledon to Aldgate."""
        tubestations = ts()
        self.assertEqual(tubestations.balance('Wimbledon', 'Aldgate'), 3.20)

    def test_case_6(self):
        """Any bus journey £1.80 Earl’s Court to Chelsea."""
        tubestations = ts()
        self.assertEqual(tubestations.balance('EarlsCourt', 'Bus'), 1.80)
    
    def test_case_7(self):
        """Test case for remaining_balance function."""
        tubestations = ts()
        self.assertEqual(tubestations.remaining_balance(10), 10)

    def test_case_8(self):
        """Test case for card_swipe function."""
        tubestations = ts()
        self.assertEqual(tubestations.card_swipe(False), 3.20)


if __name__ == "__main__":
    unittest.main()

