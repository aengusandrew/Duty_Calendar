from tkinter import *
from Calendar import *
import time

'''
root = Tk()
root.title('HA Duty Calendar')
root.geometry("800x600")

Aengus = HouseAdvisor("Aengus")
Nikki = HouseAdvisor("Nikki")
Gorman = HouseAdvisor("Gorman")
DeVaun = HouseAdvisor("DeVaun")

thebois = [Aengus, Nikki, DeVaun, Gorman]

duty_cal = Duty_Calendar("c_vno4sej7ittvciiadual8v8sak@group.calendar.google.com")
duty_cal.setHAs(thebois)

frame = LabelFrame(root, padx=200, pady=30)
frame.pack(pady=400)

dutylabel = Label(frame, text=duty_cal.duty_label(), font=("Times", 40))
dutylabel.grid(row=0, column=0)
root.update()


while True:
    time.sleep(1)
    dutylabel.config(text=duty_cal.duty_label())
    root.update()


root.mainloop()
'''


class HA_GUI:
    def __init__(self):
        self.root.title('HA Duty Calendar')
        self.root.geometry("800x600")

        def submit_cal_id():
            cal_id = enter_box.get()
            self.duty_cal = Duty_Calendar(cal_id)
            cal_id_entry.destroy()
            self.run()

        cal_id_entry = Toplevel()
        cal_id_entry.title("Open new duty calendar")
        cal_id_entry.geometry("800x150")

        enter_label = Label(cal_id_entry, text="Enter your duty calendar ID: ", font=("Times", 20))
        enter_label.grid(row=0, column=0, padx=5, pady=10)

        enter_box = Entry(cal_id_entry, width=50, borderwidth=5)
        enter_box.grid(row=0, column=1, padx=5, pady=10)

        submit_btn = Button(cal_id_entry, text="Submit", command = submit_cal_id)
        submit_btn.grid(row=1, column=0, columnspan=2)

        cal_id_entry.mainloop()

    def run(self):
        Aengus = HouseAdvisor("Aengus")
        Nikki = HouseAdvisor("Nikki")
        Gorman = HouseAdvisor("Gorman")
        DeVaun = HouseAdvisor("DeVaun")

        thebois = [Aengus, Nikki, DeVaun, Gorman]
        self.duty_cal.setHAs(thebois)

        frame = LabelFrame(self.root, padx=200, pady=30)
        frame.pack(pady=400)
        dutylabel = Label(frame, text=self.duty_cal.duty_label(), font=("Times", 40))
        dutylabel.grid(row=0, column=0)
        self.root.update()


        while True:
            time.sleep(1)
            dutylabel.config(text=self.duty_cal.duty_label())
            self.root.update()


        self.root.mainloop()


    duty_cal = Duty_Calendar("")
    root = Tk()

duty = HA_GUI()