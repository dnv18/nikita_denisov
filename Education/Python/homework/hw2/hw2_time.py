import datetime
from hw2_time_dict import dict_hour, dict_min


def time():
    usr_time = input('Input your time (hh:mm): ')
    curr_time = f'{datetime.datetime.now().time()}'
    print(f'Your time: {str_time(usr_time)}')
    print(f'System time: {str_time(curr_time)}')


def str_time(x):
    x = x.split(':')
    h = int(x[0])
    m = int(x[1])
    if m == 0 and 0 <= h <= 24:
        x = f'{dict_min[m]} {dict_hour[h][0]}'
    elif 1 <= m <= 39 and m != 30 and 0 <= h <= 24:
        x = f'{dict_min[m]} {dict_hour[h][1]}'
    elif m == 30 and 0 <= h <= 24:
        x = f'{dict_min[m]} {dict_hour[h][1]}'
    elif 40 <= m <= 59 and 0 <= h <= 24:
        x = f'{dict_min[m]} {dict_hour[h][2]}'
    else:
        x = 'Please, input correct time'
    return x


time()
