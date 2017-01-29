import sys
import unittest
import time
import datetime
from lunardate import LunarDate

sys.path.insert(0, '.')
sys.path.insert(0, '../')

from koreanholiday import Holiday

gong = Holiday(lang='en')
ko_gong = Holiday(lang='ko')

current_year = datetime.datetime.now().year

class BasicTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_fixed_holiday_in_current_year(self):
        self.assertEqual(gong.newyearsday(), datetime.date(current_year, 1, 1))
        self.assertEqual(gong.independencemovementday(), datetime.date(current_year, 3, 1))
        self.assertEqual(gong.childrensday(), datetime.date(current_year, 5, 5))
        self.assertEqual(gong.memorialday(), datetime.date(current_year, 6, 6))
        self.assertEqual(gong.constitutionday(), datetime.date(current_year, 7, 17))
        self.assertEqual(gong.liberationday(), datetime.date(current_year, 8, 15))
        self.assertEqual(gong.nationalfoundationday(), datetime.date(current_year, 10, 3))
        self.assertEqual(gong.hangulday(), datetime.date(current_year, 10, 9))
        self.assertEqual(gong.christmas(), datetime.date(current_year, 12, 25))
    
    def test_lunar_holiday_in_current_year(self):
        self.assertEqual(gong.lunarnewyearsday(), LunarDate(current_year, 1, 1).toSolarDate())
        self.assertEqual(gong.buddhasbirthday(), LunarDate(current_year, 4, 8).toSolarDate())
        self.assertEqual(gong.koreanthanksgiving(), LunarDate(current_year, 8, 15).toSolarDate())

if __name__ == '__main__':
    unittest.main()
