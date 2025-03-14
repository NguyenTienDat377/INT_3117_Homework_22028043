import unittest
from loan_eligibility import loan_eligibility

class ControlFlowTesting(unittest.TestCase):
    #Path 1
    def test_case_1(self):
        with self.assertRaises(ValueError) as context:
            loan_eligibility(-1, 75000, 540)
        self.assertEqual(str(context.exception), "Invalid age")
    
    #Path 2
    def test_case_2(self):
        with self.assertRaises(ValueError) as context:
            loan_eligibility(18, -10000, 360)
        self.assertEqual(str(context.exception), "Invalid income")

    #Path 3
    def test_case_3(self):
        with self.assertRaises(ValueError) as context:
            loan_eligibility(36, 100000, -100)
        self.assertEqual(str(context.exception), "Invalid credit score")

    #Path 4
    def test_case_4(self):
        eligible = loan_eligibility(16, 30000, 450)
        self.assertEqual(eligible, False)
    
    #Path 5
    def test_case_5(self):
        eligible = loan_eligibility(19, 25000, 450)
        self.assertEqual(eligible, False)
    
    #Path 6
    def test_case_6(self):
        eligible = loan_eligibility(20, 35000, 50)
        self.assertEqual(eligible, False)

    #Path 7
    def test_case_7(self):
        eligible = loan_eligibility(21, 40000, 320)
        self.assertEqual(eligible, True)

if __name__ == "__main__":
    unittest.main()
