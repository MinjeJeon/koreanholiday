import datetime
import tempfile
import locale

from lunardate import LunarDate
from collections import Iterable, defaultdict

# weekdays
MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


def is_iter(obj):
    return isinstance(obj, Iterable) and not isinstance(obj, (str, bytes))


class HolidayCore:

    HOLIDAYS_NAME = [
        'newyearsday', 'lunarnewyearsday', 'independencemovementday', 'arborday', 'childrensday',
        'buddhasbirthday', 'memorialday', 'constitutionday', 'liberationday', 'koreanthanksgiving',
        'nationalfoundationday', 'hangulday', 'christmas'
    ]
    DESCRIPTION = {
        'en': [
            "New Year's Day(Sinjeong)", "Lunar New Year's Day(Seolnal)",
            "Independence Movement Day(Samiljeol)", "Korean Arbor Day(Sikmokil)", "Children's Day(Eorininal)",
            "Buddha's Birthday(Seokgatansinil)", "Memorial Day(Hyeonchung-il)",
            "Constitution Day(Jeheonjeol)", "Liberation Day(Gwangbokjeol)", "Korean Thanksgiving(Chuseok)",
            "National Foundation Day(Gaecheonjeol)", "Hangul Day(Hangeulnal)", "Christmas"
        ],
        'ko': ['신정', '설날', '삼일절', '식목일', '어린이날', '석가탄신일', '현충일', '제헌절', '광복절', '추석', '개천절', '한글날', '크리스마스']
    }

    LOCALE_MAP = {'ko_KR': 'ko', 'ko': 'ko', 'korean': 'ko'}

    FIVE_DAY_WORKWEEK = datetime.date(2014, 7, 1)

    @property
    def special(self):
        if self.special is None:
            self._special = self._get_special(self.online)
        return self._special

    @property
    def today(self):
        return datetime.date.today()

    @property
    def thisyear(self):
        return datetime.date.today().year

    @staticmethod
    def yesterday(date):
        return date - datetime.timedelta(days=1)

    @staticmethod
    def tomorrow(date):
        return date + datetime.timedelta(days=1)

    @staticmethod
    def ttatomorrow(date):
        return date + datetime.timedelta(days=2)

    @staticmethod
    def threedays(date):
        return [date - datetime.timedelta(days=1), date, date + datetime.timedelta(days=1)]

    def isworkingday(self, date=None):
        date = date if date else self.today
        weekday = date.weekday()
        if date >= self.FIVE_DAY_WORKWEEK:
            return weekday in [5, 6] or date in self.holidays(date.year)
        else:
            return weekday == 6 or date in self.holidays(date.year)

    def nextworkingday(self, date=None):
        date = date if date else self.today
        while True:
            nextday = self.tomorrow(date)
            if self.isworkingday(nextday):
                return nextday


class SpecialHolidays:
    def __init__(self):
        pass


class Holiday:
    def __init__(self, online=True, lang=None):
        self.core = HolidayCore()
        self.online = online
        self.timestamp = datetime.datetime.now()

        if lang is None:
            lang, _ = locale.getdefaultlocale()
        try:
            self.lang = self.core.LOCALE_MAP[lang]
        except KeyError:
            self.lang = 'en'

        self.desc = {k: v for k, v in zip(self.core.HOLIDAYS_NAME, self.core.DESCRIPTION[self.lang])}

        self._special = None
        self._holidays_except_substitute = {}
        self._holidays = {}


    def newyearsday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = datetime.date(year, 1, 1)
        if dayoff:
            if 1999 <= year:
                return theday
            elif 1991 <= year < 1999:
                return [theday, theday + datetime.timedelta(days=1)]
            elif 1950 <= year < 1991:
                return [theday, theday + datetime.timedelta(days=1), theday + datetime.timedelta(days=2)]
            else:
                return None
        else:
            if 1896 <= year:
                return theday
            else:
                return None

    def lunarnewyearsday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = LunarDate(year, 1, 1).toSolarDate()
        if dayoff:
            if 2014 <= year:
                if substitute:
                    return self.core.threedays(theday)
                else:
                    return self.core.threedays(theday)
            elif 1989 <= year < 2014:
                return self.core.threedays(theday)
            elif 1985 <= year < 1989:
                return theday
            else:
                return None
        else:
            return theday

    def independencemovementday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = datetime.date(year, 3, 1)
        if dayoff:
            if 1946 <= year:
                return theday
            else:
                return None
        else:
            if 1920 <= year:
                return theday
            else:
                return None

    def arborday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = datetime.date(year, 4, 5)
        if dayoff:
            if 2006 <= year:
                return None
            elif 1948 <= year < 2006:
                return theday
            else:
                return None
        else:
            if 1946 <= year:
                return theday
            else:
                return None

    def childrensday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = datetime.date(year, 5, 5)
        if dayoff:
            if 1970 <= year:
                return theday
            else:
                return None
        else:
            if 1946 <= year:
                return theday
            else:
                return None

    def buddhasbirthday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = LunarDate(year, 4, 8).toSolarDate()
        if dayoff:
            if 1975 <= year:
                return theday
            else:
                return None
        else:
            return theday

    def memorialday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = datetime.date(year, 6, 6)
        if 1956 <= year:
            return theday
        else:
            return None

    def constitutionday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = datetime.date(year, 7, 17)
        if dayoff:
            if 1950 <= year < 2008:
                return theday
            else:
                return None
        else:
            if 1950 <= year:
                return theday
            else:
                return None

    def liberationday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = datetime.date(year, 8, 15)
        if 1950 <= year:
            return theday
        else:
            return None

    def koreanthanksgiving(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        theday = LunarDate(year, 8, 15).toSolarDate()
        if dayoff:
            return self.core.threedays(theday)
        else:
            return theday

    def nationalfoundationday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        return datetime.date(year, 10, 3)

    def hangulday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        return datetime.date(year, 10, 9)

    def christmas(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.core.thisyear
        return datetime.date(year, 12, 25)

    # substitute holiday

    def holidays_before_substitution(self, year=None, output='desc'):
        year = year if year else self.core.thisyear
        if year not in self._holidays_except_substitute:
            self._holidays_except_substitute[year] = self._get_holidays_before_substitution(year)
        result = self._holidays_except_substitute[year]
        if output == 'date':
            return result
        elif output == 'desc':
            return {k: ', '.join(self.desc[i] for i in v) for k, v in result}
        else:
            return result

    def _get_holidays_before_substitution(self, year=None):
        dayoffs_res = defaultdict(list)
        for hd in self.core.HOLIDAYS_NAME:
            dayoff = getattr(self, hd)(year, dayoff=True, substitute=False)
            if not is_iter(dayoff):
                dayoff = dayoff,
            for x in dayoff:
                if x is not None:
                    dayoffs_res[x].append(hd)
        return dayoffs_res

    def substitute(self, date):
        if not isinstance(date):
            date = [date]

    def holidays(self, year=None):
        year = year if year else self.core.thisyear
        if year not in self._holidays:
            self._holidays[year] = self._get_holidays(year)
        return self._holidays[year]

    def _get_holidays(self, year=None):
        year = year if year else self.core.thisyear
        before_substitute = self.holidays_before_substitution(year)

        pass

    def refresh(self, online=True):
        self._holidays_except_substitute = {}
        self._holidays = {}

    def _get_special(self, online, refresh=None):
        if self.online:
            pass
        else:
            pass

    def __getitem__(self, key):
        return self.holidays(key)


def _holidays_with_desc():
    pass