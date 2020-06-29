from struct import unpack
from logging import Logging

MASTER_ADDR = ("192.168.43.44", 2000)

class Main:
    def __init__(self):
        self.LOGGING = Logging(MASTER_ADDR)

    def run(self):
        self.LOGGING.run()
        while True:
            try:
                deg, pwr = unpack("Hf", self.LOGGING.read())
                print("Degree:", deg, "Power:", pwr)
            except KeyboardInterrupt:
                exit()
            except Exception as e:
                print("Exception:", e)

if __name__ == "__main__":
    M = Main()
    M.run()
