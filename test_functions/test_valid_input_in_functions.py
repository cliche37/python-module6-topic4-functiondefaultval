import unittest
from more_functions.validate_input_in_functions import score_input


class FunctionTests(unittest.TestCase):

    def test_score_input_test_name(self):
        self.assertEqual("Syed: 0", score_input("Syed"))

    def test_score_input_test_score_valid(self):
        self.assertEqual("Syed: 34", score_input("Syed", 34))

    def test_score_input_test_score_below_range(self):
        self.assertEqual("Invalid test score, try again!", score_input("Syed", -300))

    def test_score_input_test_score_above_range(self):
        self.assertEqual("Invalid test score, try again!", score_input("Syed", 300))

    def test_test_score_non_numeric(self):
        self.assertEqual("Invalid test score, try again!", score_input("Syed", "j"))

    def test_score_input_invalid_message(self):
        self.assertEqual("Wrong input, please try again!", score_input("Syed", 500, "Wrong input, please try again!"))

if __name__ == "__main__":
    unittest.main()