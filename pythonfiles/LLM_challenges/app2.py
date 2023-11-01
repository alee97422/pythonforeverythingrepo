import tkinter as tk
from tkinter import filedialog
import pandas as pd

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        df = pd.read_csv(filepath)
        rows, columns = df.shape
        num_nan = df.isnull().sum().sum()
        label1.config(text=f"Number of rows x columns: {rows} x {columns}")
        label2.config(text=f"Number of NaN values: {num_nan}")

root = tk.Tk()

browse_button = tk.Button(root, text="Browse for CSV file", command=browse_file)
browse_button.pack(pady=10)

label1 = tk.Label(root, text="")
label1.pack()

label2 = tk.Label(root, text="")
label2.pack()

root.mainloop()