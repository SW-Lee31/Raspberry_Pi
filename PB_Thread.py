# interrupt with thread

import RPi.GPIO as g
import time
import threading

g.setmode(g.BCM)
handler1Flag = True
handler2Flag = True

def handler1(channel):
    print("handler1 인터럽트 발생")
    Handler1Thread().start()

def handler2(channel):
    print("handler2 인터럽트 발생")
    Handler2Thread().start()

class Handler1Thread(threading.Thread):
    def run(self):
        while handler1Flag:
            print("handler1")
            time.sleep(1)

class Handler2Thread(threading.Thread):
    def run(self):
        while handler2Flag:
            print("handler2")
            time.sleep(1)

# linux kernel epoll
g.setup(24, g.IN, pull_up_down=g.PUD_DOWN)
g.setup(23, g.IN, pull_up_down=g.PUD_DOWN)
g.add_event_detect(24, g.RISING, callback=handler1, bouncetime=300)
g.add_event_detect(23, g.RISING, callback=handler2, bouncetime=300)

if __name__ == "__main__":
    while True:
        time.sleep(0.1)
