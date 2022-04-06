from calendar import month
from datetime import datetime, time, timedelta


users = {'Alex':'2000-04-07',\
        'Jane':'2000-04-08',\
        'Bob':'2000-04-11',\
        'Smith':'2000-04-08',\
        'Serega':'2000-04-09',\
        'Sam':'2000-04-10',\
        'Alin':'2000-04-19',\
        'Maria':'2000-04-09',\
        'MJ':'2000-04-12'}

def happy_birthday(names_of_workers):
    current_datetime = datetime.now()
    i = 0
    day_of_week = current_datetime.weekday()
    brth_on_holydays = []
    while i<7:
        one_wth_brthday = []
        for key,value in names_of_workers.items():
            value_transl = value.split('-')
            value_date = datetime(year=int(value_transl[0]),month=int(value_transl[1]),day=int(value_transl[2]))
            birthday_of_empl = current_datetime + timedelta(days=i)
            if value_date.day == birthday_of_empl.day:
                if value_date.month == birthday_of_empl.month:
                    one_wth_brthday.append(key)
                    day_of_week = birthday_of_empl.weekday()
                    if 4< day_of_week < 7:
                        brth_on_holydays.append(key)
                    continue
        if day_of_week == 0:
            one_wth_brthday = one_wth_brthday + brth_on_holydays
        if 4< day_of_week < 7:
            i+=1
            continue 
        if len(one_wth_brthday) != 0:
            print(birthday_of_empl.strftime('%A : '), ', '.join(one_wth_brthday))
        i+=1



happy_birthday(users)
    
    
    
    
    # if current_datetime.weekday() <=4:
    #     start_of_week = 
    