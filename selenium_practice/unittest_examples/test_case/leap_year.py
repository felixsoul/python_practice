class LeapYear:
    def __init__(self, year) -> None:
        self.year = int(year)
    
    def answer(self):
        year = self.year
        if year % 100 == 0:
            if year%400 == 0:
                return("{}是闰年".format(year))
            else:
                return("{}不是闰年".format(year))
        else:
            if year % 4 ==0:
                return("{}是闰年".format(year))
            else:
                return("{}不是闰年".format(year))
            