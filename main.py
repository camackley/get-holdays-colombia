from datetime import date

import holidays

if __name__ == "__main__":
    co_holidays = holidays.CountryHoliday('CO')
    
    year_days = [[],[],[],[],[],[],[],[],[],[],[],[]]
    
    i=1
    j=0
    monts_31 = [1,3,5,7,8,10,12]
    for month in year_days:
        if i == monts_31[j]:
            for day in range(1, 32):
                month.append(day)
            j+=1
        elif i == 2:
            for day in range(1, 30):
                month.append(day)
        else:
            for day in range(1, 31):
                month.append(day)
        i+=1
    #print(year_days)
    
    holidays_list=[]
    i=1
    for month in year_days:
        for day in month:
            if date(2020, i, day) in co_holidays:
                holidays_list.append(f'2020/{i}/{day}')
        i+=1
    
    for holiday in holidays_list:
        print(holiday)
            
                