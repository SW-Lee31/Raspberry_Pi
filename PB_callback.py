# PB_callback

import RPi.GPIO as g
import time

g.setmode(g.BCM)
cnt = 0

def handler(channel):
    global cnt # 전역변수로 선언된 것을 사용
    cnt += 1
    print(cnt)

if __name__ == "__main__":
    # linux kernel epoll
    g.setup(24, g.IN, pull_up_down=g.PUD_DOWN)
    g.add_event_detect(24, g.RISING, callback=handler, bouncetime=300)

    while True:
        time.sleep(1)
        
