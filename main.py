import tkinter as tki
import tkinter.messagebox
import sqlite3

import TitleLabel
from WoozekButton import WoozekButton
import NoncommercialSunday

root = tki.Tk()
root.title("Woozek")
root.iconbitmap("myIcon.ico")
logo = TitleLabel.TitleLabel(root)

frame_items = tki.Frame(root)
frame_items.pack()

listbox_items = tki.Listbox(frame_items, height=15, width=50, bg='#edede9')
listbox_items.pack(side=tki.LEFT)

scrollbar_items = tkinter.Scrollbar(frame_items)
scrollbar_items.pack(side=tki.RIGHT, fill=tki.Y)

listbox_items.config(yscrollcommand=scrollbar_items.set)
scrollbar_items.config(command=listbox_items.yview)

entry_item = tkinter.Entry(root, width=50)
entry_item.pack()

root.configure(background='#e3d5ca')

sundays = NoncommercialSunday.NoncommercialSunday(root)
wb = WoozekButton(root, entry_item, listbox_items)


root.mainloop()
