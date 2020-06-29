from socket import *
from threading import Thread
from serial import Serial
import data_gv
from time import sleep

class Logging:
    def __init__(self, master_addr):
        self.log_sock = socket(AF_INET, SOCK_DGRAM)
        self.log_sock.bind(master_addr)
        self.packed_data = None
        self.serve = True

    def run(self):
        t = Thread(target = self._read)
        t.start()

    def _read(self):
        while self.serve:
            try:
                self.packed_data = self.log_sock.recv(1024)
                # print("packed_data", self.packed_data)
            except:
                print("log exc")
                pass

    def read(self):
        return self.packed_data

    def __del__(self):
        self.log_sock.close()
        self.serve = False


class serialLogging:
    def __init__(self, serial_port, baud_rate = 9600):
        self.serve = True
        try:
            self.ser = Serial(serial_port, baud_rate, timeout = 0.001)
        except:
            print("Serial Fail To Initialize")

    def run(self):
        t = Thread(target = self._read)
        t.start()

    def _read(self):
        while self.serve:
            # print(data_gv.data)
            raw = self.ser.readline()
            # print("RAW", raw)
            
            if raw != b"":
                try:
                    try:
                        # print(raw[0])
                        # data_gv.data[raw[0]] = (raw[1] / 255 * 5) ** 2 / 10
                        data_gv.data[raw[0]] = (raw[1] / 255 * 5)
                    except:
                        data_gv.data.update({raw[0]: (raw[1] / 255 * 5)})
                except:
                    pass
                    # print("=======", raw)
            
            sleep(0.05)
            
            

    def __del__(self):
        self.serve = False


if __name__ == "__main__":
    SL = serialLogging('/dev/cu.usbmodem141401')
    SL.run()