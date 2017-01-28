import datetime
import tempfile

from lunardate import LunarDate

class Holiday:
    def __init__(self, online=True, refresh=False):
        self.online = online
        self._special = None
        self.timestamp = datetime.datetime.now()
        
        if refresh:
            self._special = self._get_special(self.online, refresh=True)
    
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
    
    def newyearsday(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        return datetime.date(year, 1, 1)
    
    def koreannewyear(self, year=None, dayoff=False):
        year = year if year else self.thisyear
        
    
    def _get_special(self, online, refresh=None):
        if self.online:
            pass
        else:
            pass        
