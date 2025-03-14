import unittest
from loan_eligibility import loan_eligibility

class BlackBoxTesting(unittest.TestCase):
    def test_boundaries_age(self):
        income = 31000
        credits_score = 650
        test_cases = [
            (-1 , "Invalid time"),
            (17, False),
            (18, True),
            (64, True),
            (65, True),
            (66, False),
            (101, "Invalid time")
        ]

        for age, expected_output in test_cases:
            with self.subTest(age=age):
                if isinstance(expected_output, str):
                    with self.assertRaises(ValueError) as error_context:
                        loan_eligibility(age=age, income=income, credit_score=credits_score)
                    self.assertEqual(str(error_context), expected_output)
                
                else:
                    output = loan_eligibility(age=age, income=income, credit_score=credits_score)
                    self.assertAlmostEqual(output, expected_output, places=7)
    

