# Shift servo to degree
# Read the power generated
# Log the deg and pwr to PC

from struct import pack

from logging import Logging
from anal_read import analRead
from servo import Servo

MASTER_ADDR = ("192.168.43.44", 2000)
BCM_PORT = 0
ANAL_PORT = 0

DEG_BOTTOM = 0
DEG_UPPER = 180

class Main:
    def __init__(self):
        self.LOGGING = Logging(MASTER_ADDR)
        self.ANAL_READ = analRead(ANAL_PORT)
        self.SERVO = Servo(BCM_PORT, 90)

    def run(self):
        while True:
            try:
                for deg in range(DEG_BOTTOM, DEG_UPPER + 1):
                    self.SERVO.change_deg(deg)
                    pwr = self.ANAL_READ.read_pwr(10)
                    self.LOGGING.log(pack("Hf", deg, pwr))
            except KeyboardInterrupt:
                exit()
            except Exception as e:
                print("Exception:", e)


if __name__ == "__main__":
    M = Main()
    M.run()
