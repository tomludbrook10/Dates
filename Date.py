import re

""""
Creates a date object which will contain functionality: 
Validate dates such that; 
Correct format,
between the years 1753 and 3000 and
separted by either '/', '-' or ' '. 
Also, will have functions return day, month and year. 

Author: Thomas Ludbrook
"""


class Date: 

    def __init__(self, dateIn): 
        
        #check format/ sepeartors 
        
        self.dateArr , separators = self.returnDateOp(dateIn)
        self.currError = ""
        self.check = True

        #check format of the date object. 
        try:      
            self.checkFormat(separators)
            self.checkYear()
            self.checkMonth()
            self.checkDay()
        except ValueError:
            print(dateIn , self.currError)
            self.check = False

    def returnCheck(self): 
        return self.check


    def getDay(self): 
        return self.dateArr[0]

    def getMonth(self):
        return self.dateArr[1]

    def getYear(self):
        return self.dateArr[2]

    def getFormattedDate(self):
        months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        return '{} {} {}'.format(self.dateArr[0], months[self.dateArr[1] - 1].title(), self.dateArr[2])

    def checkDay(self): 

        monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]

        if(not self.dateArr[0].isdigit()): 
            self.currError = " - INVALID: Day needs to be a number"
            raise ValueError 

        #Accounting for leap years. 
        if(self.dateArr[2] % 4 == 0): 
            if(str(self.dateArr[2])[2:] == "00" and self.dateArr[2] % 400 == 0):
                monthDays[1] = 29
        elif( not (str(self.dateArr[2])[2:] == "00")):
            monthDays[1] = 29
    
        self.dateArr[0] = int(self.dateArr[0])

        if(self.dateArr[0] < 1 or self.dateArr[0] > monthDays[self.dateArr[1] - 1]): 
            self.currError = " - INVALID: Day is not in the range of the selected month"
            raise ValueError 



    def checkMonth(self): 

        months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        
        if(self.dateArr[1].isdigit()): 
            self.dateArr[1] = int(self.dateArr[1])
            if(self.dateArr[1] < 0 or self.dateArr[1] > 12): 
                self.currError =  " - INVALID: Month needs to be 1-12"
                raise ValueError
        else: 
            if(not self.dateArr[1].lower() in months):
                self.currError = " - INVALID: Not a valid month"
                raise ValueError

            if(not (self.dateArr[1].isupper() or self.dateArr[1].islower() or self.dateArr[1].istitle())):
                self.currError = " - INVALID: Month is not in the correct format try: mmm, MMM, Mmm"
                raise ValueError

            self.dateArr[1]  = months.index(self.dateArr[1]) + 1 
         


    def checkYear(self): 
        
        if(not self.dateArr[2].isdigit()): 
            self.currError = " - INVALID: Year try yyyy or yy"
            raise ValueError    

        self.dateArr[2] = int(self.dateArr[2])

        if(self.dateArr[2] < 100): 
            if(self.dateArr[2] < 50):
                self.dateArr[2] += 2000
            else: 
                self.dateArr[2] += 1900
        
        if(self.dateArr[2] < 1753 or self.dateArr[2] > 3000): 
            self.currError = " - INVALID: Year must be within 1753-3000"
            raise ValueError 

    
        
    def checkFormat(self ,separators):
        if(len(separators) != 2): 
            self.currError = " - INVALID: must only use 2 of the same separators: \ , - or <space>,"
            raise ValueError 

        if(len(self.dateArr) != 3): 
            self.currError = " - INVALID: too many arguments try dd/mm/yyyy" 
            raise ValueError

        # checks that only one type of seperator is used. 
        if(len(set(separators)) != 1): 
            self.currError =  " - INVALID: must use just one seperator"
            raise ValueError 

    def returnDateOp(self, date):

        date = date.strip('\n')
        dateArr = re.split('-|\s|/', date)
        separators = re.sub(r'[^-|\s|/]', '', date)

        return dateArr , separators


