import datetime
import tempfile

from lunardate import LunarDate

class Holiday:

    HOLIDAYS_NAME = ['newyearsday', 'lunarnewyearsday', 'independencemovementday',
                     'arborday', 'childrensday', 'buddhasbirthday',
                     'memorialday', 'constitutionday', 'liberationday',
                     'koreanthanksgivingday', 'nationalfoundationday', 'hangulday',
                     'christmas']
    DESCRIPTION = {
        'en' : ["New Year's Day(Sinjeong)", "Lunar New Year's Day(Seolnal)", "Independence Movement Day(Samiljeol)",
                "Korean Arbor Day(Sikmokil)", "Children's Day(Eorininal)", ],
        'ko' : ['신정', '설날', '삼일절',
                '식목일', '어린이날', '석가탄신일',
                '현충일', '제헌절', '광복절',
                '추석', '개천절', '한글날',
                '크리스마스']
        } 

    def __init__(self, online=True, refresh=False, lang='en'):
        self.online = online
        self.timestamp = datetime.datetime.now()
        self

        self._special = None
        self._holidays_except_alternative = {}
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
    
    def newyearsday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return datetime.date(year, 1, 1)
    
    def lunarnewyearsday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        theday = LunarDate(year, 1, 1).toSolarDate()
        if dayoff:
            return self.threedays(theday)
        else:
            return theday
        
    def independencemovementday(self, year=None, dayoff=False):
        year = year if year else self.thisyear 
        return datetime.date(year, 3, 1)
    
    def arborday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        theday = datetime.date(year, 4, 5)
        if dayoff:
            if 1948 <= year < 2006:
                return theday
        else:
            return None  
    
    def childrensday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return datetime.date(year, 5, 5)
    
    def buddhasbirthday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return LunarDate(year, 4, 8).toSolarDate()

    def memorialday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return datetime.date(year, 6, 6)
    
    def constitutionday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        theday = datetime.date(year, 7, 17)
        if dayoff:
            if 1950 <= year < 2008:
                return theday
            else:
                return None
    
    def liberationday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return datetime.date(year, 8, 15)
    
    def koreanthanksgivingday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        theday = LunarDate(year, 8, 15).toSolarDate()
        if dayoff:
            return self.threedays(theday)
        else:
            return theday
    
    def nationalfoundationday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return datetime.date(year, 10, 3)
    
    def hangulday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return datetime.date(year, 10, 9)
    
    def christmas(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return datetime.date(year, 12, 25)


    #alternative holiday

    def holidays_except_alternative(self, year=None):
        year = year if year else self.thisyear

    def isworkday(self, date):
        pass

    def refresh(online=True):
        pass
        
    
    def _get_special(self, online, refresh=None):
        if self.online:
            pass
        else:
            pass        
