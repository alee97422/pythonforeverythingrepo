import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.style = Style(theme='flatly')
        self.root.title('Budget Management')

        self.bill_list = []

        self.setup_ui()



    def setup_ui(self):
        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Input field to add bills
        self.bill_var = tk.StringVar()
        bill_entry = ttk.Entry(frame, textvariable=self.bill_var)
        bill_entry.grid(row=0, column=0)

        add_button = ttk.Button(frame, text='Add Bill', command=self.add_bill)
        add_button.grid(row=0, column=1, padx=10)

        # List to show bills
        self.listbox = tk.Listbox(frame, width=40)
        self.listbox.grid(row=1, column=0, columnspan=2, pady=10)

        # Buttons to mark bills as paid or unpaid
        paid_button = ttk.Button(frame, text='Mark as Paid On time', command=self.mark_paid)
        paid_button.grid(row=2, column=0, pady=10)

        unpaid_button = ttk.Button(frame, text='Mark as Paid late', command=self.mark_unpaid)
        unpaid_button.grid(row=2, column=1, pady=10)

    def add_bill(self):
        bill = self.bill_var.get()
        if bill:
            self.bill_list.append((bill, False))  # (bill, is_paid)
            self.update_listbox()

    def mark_paid(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            bill, _ = self.bill_list[index]
            self.bill_list[index] = (bill, True)  # Mark as paid
            self.update_listbox()

    def mark_unpaid(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            bill, _ = self.bill_list[index]
            self.bill_list[index] = (bill, False)  # Mark as unpaid
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for bill, is_paid in self.bill_list:
            status = 'Paid on time' if is_paid else 'Paid Latec'
            self.listbox.insert(tk.END, f'{bill} - {status}')

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
