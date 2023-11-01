import tkinter as tk
import pandas as pd
from tkinter import filedialog

# Define the main window
window = tk.Tk()
window.title("CSV File Viewer")

# Function to open a file using the built-in dialog box
def open_file():
    # Open the dialog box to select the file
    file_path = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("CSV files", "*.csv"), ("Excel files", "*.xlsx")))

    if file_path:
        # Load the selected file as a Pandas DataFrame
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            # If the selected file is not a CSV, retry with Excel file format
            df = pd.read_excel(file_path)

        # Print the number of columns and rows to a label
        columns_rows_label = tk.Label(text="Number of columns: " + str(df.shape[1]) + " \nNumber of rows: " + str(df.shape[0]))
        columns_rows_label.pack()

        # Print the number of NaN values to a label
        nan_values_label = tk.Label(text="Number of NaN values: " + str(df.isnull().sum().sum()))
        nan_values_label.pack()

# Create the GUI
window.geometry("400x300")

# Create the file input button
file_input_button = tk.Button(text="Browse for file", command=open_file)
file_input_button.pack()

# Start the event loop
window.mainloop()