from tkinter import *
r =  Tk()

my_entries = []
for i in range(5):
    e = Label(r, text=i)
    my_entries.append(e)
    e.pack(side='top')
    
r.after(4000, lambda: my_entries[2].configure(text='Example'))
r.mainloop()