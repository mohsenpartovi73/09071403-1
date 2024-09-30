import datetime

now = datetime.datetime.now()
year_now = now.year
for i in range(1):    
    year = int(input('year :'))
    if year > 2023 and year < 1900:
        print('wrong year')
    month = int(input('month:'))
    if month > 12:
        print('wrong month')
    day = int(input('day:'))
    if day > 31:
        print('wrong day')

    age = year_now  - year
    print('your birthday is on :{}/{}/{}'.format(year,month,day))
    print('your age is:',age)    






