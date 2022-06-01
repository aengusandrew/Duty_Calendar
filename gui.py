from tkinter import *
from Calendar import *
import time

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

        settings_btn = Button(self.root, text="S", command=self.settings)
        settings_btn.pack(padx=10, pady=10, anchor="ne")

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

    def settings(self):
        sett_window = Toplevel()
        sett_window.geometry("400x600")
        sett_window.title("Settings")

        main_lbl = Label(sett_window, text="Settings", font=("Times", 30))
        main_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        def save():
            self.duty_cal.in_room = in_room_var.get()

            sett_window.destroy()

        def addHA():
            newHA_name = add_HA_entry.get()
            newHA = HouseAdvisor(newHA_name)
            self.duty_cal.HAs.add(newHA)
            add_HA_entry.delete(0, END)

        # HA is in their room
        in_room_var = BooleanVar()
        in_room_btn = Checkbutton(sett_window, text="HA is in room", variable=in_room_var, onvalue=True, offvalue=False)
        in_room_btn.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        # Add an HA
        add_HA_lbl = Label(sett_window, text="New HA name: ")
        add_HA_lbl.grid(row=2, column=0, padx=10)

        add_HA_entry = Entry(sett_window, width=15)
        add_HA_entry.grid(row=2, column=1, padx=10)

        add_HA_btn = Button(sett_window, text="Add", command=addHA)
        add_HA_btn.grid(row=2, column=2, padx=10)

        # TODO: Add a checklist to delete HAs

        save_button = Button(sett_window, text="Save", command=save)
        save_button.grid(row=3, column=0)




    # TODO: Add a function that is passed a Tkinter Entry widget as argument and then creates a new window which is a
    #   keyboard that can be used as an on screen keyboard

    # TODO: Add a similar function which does the same thing but for a number pad

    duty_cal = Duty_Calendar("")
    root = Tk()

duty = HA_GUI()