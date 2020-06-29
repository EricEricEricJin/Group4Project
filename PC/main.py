from GUI import GUI
from data_gv import data
from read_log import serialLogging

MASTER_ADDR = ("127.0.0.1", 2000)

if __name__ == "__main__":
    SLOGGING_ins = serialLogging('/dev/cu.usbmodem142401')
    GUI_ins = GUI()
    SLOGGING_ins.run()
    GUI_ins.run()
    print("WINDOW CLOSED")
    del(SLOGGING_ins)