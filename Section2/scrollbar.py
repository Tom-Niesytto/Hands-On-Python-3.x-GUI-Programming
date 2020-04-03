import tkinter as tk

win = tk.Tk()

win.configure(background="#808000")

frame1 = tk.Frame(win,width=80, height=80,bg = '#ffffff',borderwidth=1, relief="sunken")
scrollbar = tk.Scrollbar(frame1) 
editArea = tk.Text(frame1, width=10, height=10, wrap="word",
                   yscrollcommand=scrollbar.set,
                   borderwidth=0, highlightthickness=0)
scrollbar.config(command=editArea.yview)
scrollbar.pack(side="right", fill="y")
editArea.pack(side="left", fill="both", expand=True)
frame1.place(x=10,y=30)

win.mainloop()