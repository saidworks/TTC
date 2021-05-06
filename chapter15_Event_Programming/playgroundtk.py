import tkinter
class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.increase_button = tkinter.Button(self)
        self.increase_button["text"] = "Increase"
        self.increase_button["command"] = self.increase_value
        self.increase_button.pack(side="right")
        self.increase_button = tkinter.Button(self)
        self.increase_button["text"] = "Decrease"
        self.increase_button["command"] = self.decrease_value
        self.increase_button.pack(side="left")
    def increase_value(self):
        global mainval
        mainval *= 2
        print (mainval)
    def decrease_value(self):
        global mainval
        mainval /= 2
        print (mainval)
mainval = 1.0
root = tkinter.Tk()
app = Application(master=root)
app.mainloop()