#url: https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program
import tkinter as tk

class Application(tk.Frame):
    #constructor with default
    def __init__(self, master=None):
        print(type(master))
        super().__init__(master)
        self.master = master
        print(type(self))
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #why are button created as class attributes 
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
print(type(root))
app = Application(master=root)
app.mainloop()