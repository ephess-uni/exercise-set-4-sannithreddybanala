""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    date_str = datestr.split('T')[0]
    time_str = datestr.split('T')[1]
    date_list = date_str.split('-')
    time_list = time_str.split(':')
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    hour = int(time_list[0])
    minutes = int(time_list[1])
    seconds = int(time_list[2])
    return datetime(year, month, day, hour, minutes, seconds)




# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')