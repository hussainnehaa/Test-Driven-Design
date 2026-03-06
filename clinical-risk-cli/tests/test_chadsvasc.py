import unittest
from clinical_risk.risk_scores import cha2ds2_vasc_score


class TestCHADS2VASc(unittest.TestCase):

    def test_age_over_75(self):
        # TODO: Write a test case for age over 75, which should contribute 2 points to the score.
        self.assertEqual(cha2ds2_vasc_score(age=80, female=False, chf=False, htn=False, dm=False, stroke=False, vascular=False), 2)

    def test_multiple_risk_factors(self):
        # TODO: Write a test case for multiple risk factors, such as age 65-74, female sex, and hypertension, which should contribute a total of 3 points to the score.
        self.assertEqual(cha2ds2_vasc_score(age=70, female=True, chf=False, htn=True, dm=False, stroke=False, vascular=False), 3)

    def test_no_risk_factors(self):
        # TODO: Write a test case for no risk factors, which should result in a score of 0.
        self.assertEqual(cha2ds2_vasc_score(age=50, female=False, chf=False, htn=False, dm=False, stroke=False, vascular=False), 0)

    def test_stroke_high_score(self):
        self.assertEqual(cha2ds2_vasc_score(age=60, female=False, chf=False, htn=False, dm=False, stroke=True, vascular=False), 2)

    def test_invalid_age_raises(self):
        with self.assertRaises(ValueError):
            cha2ds2_vasc_score(age=0, female=False, chf=False, htn=False, dm=False, stroke=False, vascular=False)
        with self.assertRaises(ValueError):
            cha2ds2_vasc_score(age=-1, female=False, chf=False, htn=False, dm=False, stroke=False, vascular=False)

    def test_invalid_bool_raises(self):
        with self.assertRaises(ValueError):
            cha2ds2_vasc_score(age=60, female="yes", chf=False, htn=False, dm=False, stroke=False, vascular=False)