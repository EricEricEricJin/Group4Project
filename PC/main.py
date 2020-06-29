from GUI import GUI
from data_gv import data
from read_log import serialLogging

MASTER_ADDR = ("127.0.0.1", 2000)
PORT = '/dev/cu.usbmodem142401'

if __name__ == "__main__":
    SLOGGING_ins = serialLogging(PORT)
    GUI_ins = GUI()
    SLOGGING_ins.run()
    GUI_ins.run()
    print("WINDOW CLOSED")
