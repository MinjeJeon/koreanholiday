import datetime
import tempfile

from lunardate import LunarDate

class Holiday:

    HOLIDAYS_NAME = ['newyearsday', 'lunarnewyearsday', '']

    def __init__(self, online=True, refresh=False):
        self.online = online
        self.timestamp = datetime.datetime.now()

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
    def threeday(date):
        return [date - datetime.timedelta(days=1), date, date + datetime.timedelta(days=1)]
    
    def newyearsday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return datetime.date(year, 1, 1)
    
    def lunarnewyearsday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        theday = LunarDate(year, 1, 1).toSolarDate()
        if dayoff:
            return self.threeday(theday)
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
