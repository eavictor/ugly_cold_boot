import pyautogui
import time
import sqlite3


def count_plus_one():
    conn = sqlite3.connect('sqlite3.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, stamp INTEGER);")
    conn.commit()
    c.execute("INSERT INTO my_table (stamp) VALUES (1);")
    conn.commit()
    count = c.execute("SELECT COUNT(*) FROM my_table;").fetchone()
    conn.close()
    print('Cold Boot Count: {}'.format(count[0]))


def auto_shutdown():
    count_plus_one()
    print('Delay 10 secs')
    time.sleep(10)
    while True:
        print('Try launching set_time_and_shutdown.exe')
        image = pyautogui.locateOnScreen('images/set_time_and_shutdown.png')
        if image is not None:
            print('Found matched image (set_time_and_shutdown.png)')
            center = pyautogui.center(image)
            pyautogui.click(center[0], center[1], clicks=1, button='right')
        else:
            print('Unable to find matched image on screen (set_time_and_shutdown.png)')

        time.sleep(2)

        image2 = pyautogui.locateOnScreen('images/run_as_administrator.png')
        if image2 is not None:
            print('Found matched image (run_as_administrator.png)')
            center2 = pyautogui.center(image2)
            pyautogui.click(center2[0], center2[1], clicks=1, button='left')
            break
        else:
            print('Unable fo find matched image on screen (run_as_administrator.png)')

        time.sleep(2)


if __name__ == '__main__':
    auto_shutdown()
