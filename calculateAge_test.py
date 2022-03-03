"""
This a Test for calculateAge
"""
import unittest
import datetime


from calculateAgeUtil import calculateAge

class TestAgeCalculation(unittest.TestCase):

    def test_calculated_age_day_before_today(self):
        birthday = datetime.datetime.strptime("22.01.2000", "%d.%m.%Y")
        today = datetime.datetime.strptime("03.03.2022", "%d.%m.%Y")
        result = calculateAge(birthday,today)
        self.assertEqual(result, 22)

    def test_calculated_age_day_after_today(self):
        birthday = datetime.datetime.strptime("22.05.2000", "%d.%m.%Y")
        today = datetime.datetime.strptime("03.03.2022", "%d.%m.%Y")
        result = calculateAge(birthday,today)
        self.assertEqual(result, 21)

if __name__ == '__main__':
    unittest.main()
    