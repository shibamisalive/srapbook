from datetime import datetime

datest = '25/12/2023'

def numberofdays(datest):
    datest = datetime.strptime(datest, '%d/%m/%Y') #converting date into a date-time object
    today = datetime.today()  #fetching todays date
    diff = today - datest  #ni of days between today and input date
    daydiff = diff.days
    print(daydiff)
    '''return daydiff  #Extract the number of days from the timedelta object'''