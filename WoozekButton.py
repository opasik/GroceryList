import tkinter as tki
import sqlite3
import pickle

class WoozekButton:

    def __init__(self, master, entry_item, listbox_items):
        frame_items = tki.Frame(master)
        frame_items.pack()
        self.master = master

        self.entry_item = entry_item
        self.listbox_items = listbox_items

        self.add_button = tki.Button(master, text="Add Item", width=41, font=("Century Gothic", 10),
                                   command=self.add_item, bg='#d6ccc2')
        self.add_button.pack()

        self.delete_button = tki.Button(master, text="Delete Item", width=41, font=("Century Gothic", 10),
                                       command=self.delete_item, bg='#d6ccc2')
        self.delete_button.pack()

        self.delete_all_button = tki.Button(master, text="Delete All Items", width=41, font=("Century Gothic", 10),
                                       command=self.delete_all_items,
                                       bg='#d6ccc2')
        self.delete_all_button.pack()

        self.save_button = tki.Button(master, text="Save Items", width=41, font=("Century Gothic", 10),
                                       command=self.save_items, bg='#d6ccc2')
        self.save_button.pack()

        self.load_button = tki.Button(master, text="Load Items", width=41, font=("Century Gothic", 10),
                                       command=self.load_items, bg='#d6ccc2')
        self.load_button.pack()

        self.clear_button = tki.Button(master, text="Clear Items", width=41, font=("Century Gothic", 10),
                                   command=self.clear_database, bg='#d6ccc2')
        self.clear_button.pack()

        self.master.bind('<Key>', self.bindings)


    def clear_database(self):
        conn = sqlite3.connect('items_database.db')
        cur = conn.cursor()

        cur.execute("DROP TABLE saved_items")
        self.listbox_items.delete(0, tki.END)
        cur.execute("CREATE TABLE IF NOT EXISTS saved_items(item text);")

        conn.commit()
        conn.close()

    def add_item(self):
        item = self.entry_item.get()
        if item == "":
            tki.messagebox.showwarning(title="Woozek warning", message="You must enter an item!")
        else:
            self.listbox_items.insert(tki.END, item)
            self.entry_item.delete(0, tki.END)

    def delete_item(self):
        try:
            item_idx = self.listbox_items.curselection()[0]
            self.listbox_items.delete(item_idx)
        except:
            tki.messagebox.showwarning(title="Woozek warning", message="Select an item!")


    def delete_all_items(self):
        self.listbox_items.delete(0, tki.END)

    def save_items(self):
        conn = sqlite3.connect('items_database.db')
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS saved_items(item text);")

        self.atuple = self.listbox_items.get(0, tki.END)
        self.alist = list(self.atuple)

        for item in self.alist:
            cur.execute("INSERT INTO saved_items (item) VALUES('" + item + "');")
        conn.commit()
        conn.close()

    def load_items(self):
        conn = sqlite3.connect('items_database.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM saved_items;")
        self.records = cur.fetchall()
        print(self.records)
        self.listbox_items.delete(0, tki.END)
        for item in self.records:
            self.listbox_items.insert(tki.END, item)

        conn.commit()
        conn.close()

    def bindings(self, event):
        if event.keysym == 'Return':
            self.add_item()
        if event.keysym == 'Delete':
            self.delete_item()

