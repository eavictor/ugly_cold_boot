import win32api
import subprocess


time_tuple = (2018, 12, 12, 23, 59, 0)


def set_sys_time():
    print('Set system time to {0}'.format(time_tuple))

    win32api.SetSystemTime(time_tuple[0],  # year
                           time_tuple[1],  # month
                           0,
                           time_tuple[2],  # day
                           time_tuple[3],  # hour
                           time_tuple[4],  # minute
                           time_tuple[5],  # second
                           0
                           )


def shutdown():
    subprocess.run(['shutdown', '/s', '/t', '0'])


if __name__ == '__main__':
    set_sys_time()
    shutdown()
