import datetime
import tempfile

from lunardate import LunarDate

# weekdays
MON, TUE, WED, THU, FRI, SAT, SUN = range(7)


class Holiday:

    HOLIDAYS_NAME = ['newyearsday', 'lunarnewyearsday', 'independencemovementday',
                     'arborday', 'childrensday', 'buddhasbirthday',
                     'memorialday', 'constitutionday', 'liberationday',
                     'koreanthanksgiving', 'nationalfoundationday', 'hangulday',
                     'christmas']
    DESCRIPTION = {
        'en': ["New Year's Day(Sinjeong)", "Lunar New Year's Day(Seolnal)", "Independence Movement Day(Samiljeol)",
               "Korean Arbor Day(Sikmokil)", "Children's Day(Eorininal)", "Buddha's Birthday(Seokgatansinil)",
               "Memorial Day(Hyeonchung-il)", "Constitution Day(Jeheonjeol)", "Liberation Day(Gwangbokjeol)",
               "Korean Thanksgiving(Chuseok)", "National Foundation Day(Gaecheonjeol)", "Hangul Day(Hangeulnal)",
               "Christmas"],
        'ko': ['신정', '설날', '삼일절',
               '식목일', '어린이날', '석가탄신일',
               '현충일', '제헌절', '광복절',
               '추석', '개천절', '한글날',
               '크리스마스']
    }

    def __init__(self, online=True, refresh=False, lang='en'):
        self.online = online
        self.timestamp = datetime.datetime.now()
        self.desc = {k: v for k, v in zip(
            self.HOLIDAYS_NAME, self.DESCRIPTION[lang])}

        self._special = None
        self._holidays_except_substitute = {}
        self._holidays = {}

        if refresh:
            self.refresh()

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
    def threedays(date):
        return [date - datetime.timedelta(days=1), date, date + datetime.timedelta(days=1)]

    def newyearsday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
        theday = datetime.date(year, 1, 1)
        if dayoff:
            if 1950 <= year < 1991:
                return [theday, theday + datetime.timedelta(days=1), theday + datetime.timedelta(days=2)]
            elif 1991 <= year < 1999:
                return [theday, theday + datetime.timedelta(days=1)]
            elif 1999 <= year:
                return theday
        else:
            if 1896 <= year:
                return theday
            else:
                return None

    def lunarnewyearsday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
        theday = LunarDate(year, 1, 1).toSolarDate()
        if dayoff:
            if 2014 <= year:
                if substitute:
                    return self.threedays(theday)
                else:
                    return self.threedays(theday)
            elif 1989 <= year < 2014:
                return self.threedays(theday)
            elif 1985 <= year < 1989:
                return theday
            else:
                return None
        else:
            return theday


    def independencemovementday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
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
        year = year if year else self.thisyear
        theday = datetime.date(year, 4, 5)
        if dayoff:
            if 1948 <= year < 2006:
                return theday
            elif 2006 <= year:
                return None
            else:
                return None
        else:
            if 1946 <= year:
                return theday
            else:
                return None

    def childrensday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
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
        year = year if year else self.thisyear
        theday = LunarDate(year, 4, 8).toSolarDate()
        if dayoff:
            if 1975 <= year:
                return theday
            else:
                return None
        else:
            return theday

    def memorialday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
        theday = datetime.date(year, 6, 6)
        if 1956 <= year:
            return theday
        else:
            return None

    def constitutionday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
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
        year = year if year else self.thisyear
        theday = datetime.date(year, 8, 15)
        if 1950 <= year:
            return theday
        else:
            return None

    def koreanthanksgiving(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
        theday = LunarDate(year, 8, 15).toSolarDate()
        if dayoff:
            return self.threedays(theday)
        else:
            return theday

    def nationalfoundationday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
        return datetime.date(year, 10, 3)

    def hangulday(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
        return datetime.date(year, 10, 9)

    def christmas(self, year=None, dayoff=False, substitute=True):
        year = year if year else self.thisyear
        return datetime.date(year, 12, 25)

    # substitute holiday

    def holidays_before_substitution(self, year=None):
        year = year if year else self.thisyear
        if year not in self._holidays_except_substitute:
            self._holidays_except_substitute[year] = self._get_holidays_before_substitution(year)
        return self._holidays_except_substitute[year]

    def _get_holidays_before_substitution(self, year=None):
        dayoffs_raw = []
        for hd in self.HOLIDAYS_NAME:
            dayoff = getattr(self, hd)(year, dayoff=True, substitute=False)
            if isinstance(dayoff, list):
                dayoffs_raw.extend(dayoff)
            else:
                dayoffs_raw.append(dayoff)
        return sorted(list(set([x for x in dayoffs_raw if x is not None])))

    def substitute(self, date):
        if not isinstance(date):
            date = [date]
            
    def holidays(self, year=None):
        year = year if year else self.thisyear
        if year not in self._holidays:
            self._holidays[year] = self._get_holidays(year)
        return self._holidays[year]

    def _get_holidays(self, year=None):
        year = year if year else self.thisyear
        before_substitute = self.holidays_before_substitution(year)
        
        pass

    def isworkingday(self, date):
        pass
    
    def nextworkingday(self, date=None):
        if date is None:
            date = self.today
        while True:
            nextday = self.tomorrow(date)
            if self.isworkingday(nextday):
                return nextday

    def refresh(self, online=True):
        pass

    def _get_special(self, online, refresh=None):
        if self.online:
            pass
        else:
            pass
