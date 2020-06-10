from datetime import date

#Import library for get holidays
import holidays

def get_all_year():
    year_days = [[],[],[],[],[],[],[],[],[],[],[],[]]
    i=1
    j=0
    months_31 = [1,3,5,7,8,10,12]
    for month in year_days:
        if i == months_31[j]:
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
    return year_days

if __name__ == "__main__":
    #Instance Holidays for a specific country
    co_holidays = holidays.CountryHoliday('CO')
    
    #Get all 2020 calendar for do a evaluation 
    year_days = get_all_year()
    
    holidays_list=[]
    i=1
    for month in year_days:
        for day in month:
            #Use a date for comparation with co_holdays object
            if date(2020, i, day) in co_holidays:
                holidays_list.append(f'2020/{i}/{day}')
        i+=1
    
    for holiday in holidays_list:
        print(holiday)