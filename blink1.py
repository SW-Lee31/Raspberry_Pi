import RPi.GPIO as gp
import time

def setup():
	gp.setmode(gp.BCM) # 핀타입 설정
	gp.setup(18, gp.OUT)
	
def loop():
	try:
		while (True):
            print("LED On")
			gp.output(18, True)
			time.sleep(1)
            print("LED Off")
			gp.output(18, False)
			time.sleep(1)
	except KeyboardInterrupt:
		print("키보드 인터럽트!")
		gp.cleanup()

if __name__ == "__main__": # 메인역할
    setup()
    loop()