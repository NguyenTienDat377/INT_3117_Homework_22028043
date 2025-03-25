import unittest
from loan_eligibility import loan_eligibility

class DataDrivenTesting(unittest.TestCase):
    def test_case1(self):
        with self.assertRaises(ValueError) as context:
            loan_eligibility(-1, 10000, 50)
        self.assertEqual(str(context.exception), "Invalid age")

    def test_case_2(self):
        eligibility = loan_eligibility(17, 5000, 30)
        self.assertEqual(eligibility, False)

    def test_case_3(self):
        eligibility = loan_eligibility(16, 17500, 60)
        self.assertEqual(eligibility, False)

    def test_case_4(self):
        eligibility = loan_eligibility(19, 25000, 75)
        self.assertEqual(eligibility, False)

    def test_case_5(self):
        with self.assertRaises(ValueError) as context:
            loan_eligibility(20, -1000, 60)
        self.assertEqual(str(context.exception), "Invalid income")

    def test_case_6(self):
        with self.assertRaises(ValueError) as context:
            loan_eligibility(21, 45000, -10)
        self.assertEqual(str(context.exception), "Invalid credit score")

    def test_case_7(self):
        eligibility = loan_eligibility(27, 25000, 70)
        self.assertEqual(eligibility, False)

    def test_case_8(self):
        eligibility = loan_eligibility(36, 50000, 45)
        self.assertEqual(eligibility, False)

    def test_case_9(self):
        with self.assertRaises(ValueError) as context:
            loan_eligibility(27, 56000, -20)
        self.assertEqual(str(context.exception), "Invalid credit score")

    def test_case_10(self):
        eligibility = loan_eligibility(22, 20000, 70)
        self.assertEqual(eligibility, False)

    def test_case_11(self):
        eligibility = loan_eligibility(18, 31000, 60)
        self.assertEqual(eligibility, True)

    def test_case_12(self):
        eligibility = loan_eligibility(20, 40000, 50)
        self.assertEqual(eligibility, False)

if __name__ == '__main__':
    unittest.main()