from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, dialog
from threading import Thread
from time import sleep
from data_gv import data
import csv

MIN_DEG = 0
MAX_DEG = 180

class GUI:
    def __init__(self):
        self.freezeText = "Freeze"
        self.freeze = False

        self.serve = True
        self.func_lines = []

        self.root = Tk()
        self.root.geometry("1280x720")
        
        self.canvas = Canvas(self.root, width = 1080, height = 720, bg = "black")
        for y in range(100):
            self.canvas.create_line(0, int(720 - y * 7.2), 1079, int(720 - y * 7.2), fill = "#505050", width = 1)
            # int((1 + x) * (1080 / (MAX_DEG - MIN_DEG + 1)))
        
        for x in range(MAX_DEG - MIN_DEG):
            self.canvas.create_line((1080 / (MAX_DEG - MIN_DEG + 1) * (1 + x)), 0, (1080 / (MAX_DEG - MIN_DEG + 1) * (1 + x)), 719, fill = "grey", width = 1)
                
        
        self.data_tv = Treeview(self.root, height = 700, show = "headings", columns = ("Power / W"))
        self.data_tv["columns"] = ["deg", "pwr"]
        self.data_tv.column("deg", width = 80)
        self.data_tv.column("pwr", width = 100)
        self.data_tv.heading("deg", text = "Degree / deg")
        self.data_tv.heading("pwr", text = "Power / W")

        self.save_button = Button(self.root, text = "SAVE", command = self._write_file)
        self.freeze_button = Button(self.root, text = self.freezeText, command = self._freeze)

        self.canvas.place(x = 0, y = 0)
        self.data_tv.place(x = 1080, y = 0)
        
        # self.yscrollbar = Scrollbar(self.root)
        # self.yscrollbar.place(x = 1270, y = 0)
        # self.yscrollbar.config(command = self.data_tv.yview)
        # self.data_tv.configure(yscrollcommand = self.yscrollbar.set)

        self.save_button.place(x = 1180, y = 700)
        self.freeze_button.place(x = 1230, y = 700)
        


    def run(self):
        t = Thread(target = self._service)
        t.start()
        self.root.mainloop()
        self.serve = False
        sleep(0.1)

    def _service(self):
        while self.serve:
            
            try:
                if self.freeze == False:
                    list_data = []
                    for deg in range(MIN_DEG, MAX_DEG + 1):
                        if deg in data:
                            list_data.append([deg, data[deg]])

                # Update table
                items = self.data_tv.get_children()
                for item in items:
                    self.data_tv.delete(item)
                
                for i in range(len(list_data)):
                    self.data_tv.insert("", i, values = (str(list_data[i][0]), str(list_data[i][1])))

                # Update graph
                # self.canvas.delete(ALL)
                for i in range(len(self.func_lines)):
                    self.canvas.delete(self.func_lines[i])
                self.func_lines = []
                # print("Data", list_data)
                for i in range(len(list_data) - 1):
                    self.func_lines.append(self.canvas.create_line(self._deg2x(list_data[i][0]), self._pwr2y(list_data[i][1]), self._deg2x(list_data[i + 1][0]), self._pwr2y(list_data[i + 1][1]), fill = "green", width = 2))
                    # print("draw line:", self._deg2x(list_data[i][0]), self._pwr2y(list_data[i][1]), self._deg2x(list_data[i + 1][0]), self._pwr2y(list_data[i + 1][1]))
                # self.canvas.place(x = 0, y = 0)
            except:
                pass
            sleep(0.2)

    def _write_file(self):
        f = filedialog.asksaveasfile()
        f_csv = csv.writer(f)
        f_csv.writerows(data)
        f.close()

    def _freeze(self):
        if self.freeze == True:
            self.freeze = False
            self.freeze_button["text"] = "Freeze"
        else:
            self.freeze = True
            self.freeze_button["text"] = "Unfreeze"

    def _deg2x(self, deg):
        return deg * 13

    def _pwr2y(self, pwr):
        return 720 - (pwr * 288)
        


if __name__ == "__main__":
    G = GUI()
    G.run()