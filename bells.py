import time
import subprocess
import datetime
import pytz
from threading import Thread
#import lcd1602_driver

pin = 10
gpiopath = "/sys/class/gpio/gpio"+str(pin)+"/value"
oldtime = ""
subprocess.call("echo "+str(pin)+" > /sys/class/gpio/export", shell=True)
subprocess.call("echo out > /sys/class/gpio/gpio"+str(pin)+"/direction", shell=True)
#lcd = lcd_driver.lcd()


class MyThread(Thread):    
    def __init__(self, duration):
        Thread.__init__(self)
        self.duration = duration
    def run(self):
        f = open('bells.log','a')
        #lcd.lcd_display_string("BELL",2)
        print("START BELL FOR "+str(self.duration)+" SECONDS")
        f.write(str(datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')))[11:19]+' '+days[datetime.datetime.now().isoweekday()]+' - '+'START BELL'+'\n')
        subprocess.call("echo 1 > "+gpiopath, shell=True)
        time.sleep(self.duration)
        subprocess.call("echo 0 > "+gpiopath, shell=True)
        #lcd.lcd_display_string("    ",2)
        print("STOP BELL")
        f.write(str(datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')))[11:19]+' '+days[datetime.datetime.now().isoweekday()]+' - '+'STOP BELL'+'\n')
        f.close()

days = ['',
        'Mon',
        'Tue',
        'Wed',
        'Thu',
        'Fri',
        'Sat',
        'Sun'
        ]

bells = [
        '09:00:00', #1 start
        '09:45:00', #1 end
        '09:55:00', #2 start
        '10:40:00', #2 end
        '10:50:00', #3 start
        '11:35:00', #3 end
        '11:55:00', #4 start
        '12:40:00', #4 end
        '13:00:00', #5 start
        '13:45:00', #5 end
        '13:55:00', #6 start
        '14:40:00', #6 end
        '14:50:00', #7 start
        '15:35:00'  #7 end
        ]

bellsSB = [
        '09:00:00', #1 start
        '09:45:00', #1 end
        '09:55:00', #2 start
        '10:40:00', #2 end
        '10:50:00', #3 start
        '11:35:00', #3 end
        '11:55:00', #4 start
        '12:40:00', #4 end
        '13:00:00', #5 start
        '13:45:00', #5 end
        '13:50:00', #6 start
        '14:35:00', #6 end
        '15:00:00', #1 shum start
        '15:45:00', #1 shum end
        '15:50:00', #2 shum start
        '16:35:00', #2 shum end
        '17:00:00', #3 shum start
        '17:45:00', #3 shum end
        '17:50:00', #4 shum start
        '18:35:00'  #4 shum end
        ]

prebells = [
        '08:58:00', #1
        '09:53:00', #2
        '10:48:00', #3
        '11:53:00', #4
        '12:58:00', #5
        '13:53:00', #6
        '14:48:00'  #7
        ]

prebellsSB = [
        '08:58:00',
        '09:53:00',
        '10:48:00',
        '11:53:00',
        '12:58:00',
        '13:48:00'
        ]

while True:
    nowtime = str(datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')))[11:19]
    wd = str(datetime.datetime.now().isoweekday())
    if (nowtime!=oldtime):
        print(nowtime)
        #lcd.lcd_display_string(days[wd-1]+' '+nowtime,1)
    if nowtime!=oldtime and wd!='7':
        if (nowtime in bells and wd!='6'):
            MyThread(4).start()
        if (nowtime in prebells and wd!='6'):
            MyThread(1).start()
        if (nowtime=='08:50:00' and wd=='1'):
            MyThread(4).start()
        if (nowtime in bellsSB and wd=='6'):
            MyThread(4).start()
        if (nowtime in prebellsSB and wd=='6'):
            MyThread(1).start()

    oldtime = nowtime
    time.sleep(0.5)
