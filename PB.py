import RPi.GPIO as g
import time

def setup():
    g.setwarnings(False)
    g.setmode(g.BCM)
    g.setup(24, g.IN)

def loop():
    cnt = 0
    while True:
        try:
            val = g.input(24)
            if val == True:
                cnt += 1
                print(cnt)
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n" + "인터럽트 발생" + "\n")
            g.cleanup()

if __name__ == "__main__":
    setup()
    loop()
