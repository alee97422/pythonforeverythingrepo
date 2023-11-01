import tkinter as tk
from tkinter import ttk
import subprocess

import os

def create_directory():
    desktop_path = os.path.expanduser("~/Desktop")  # Get the user's Desktop directory
    os.chdir(desktop_path)  # Change the current working directory to the Desktop
    path = entry_path.get()
    os.makedirs(path, exist_ok=True)  # Create the directory


def setup_virtualenv():
    path = entry_path.get()
    subprocess.run(['python', '-m', 'venv', f'{path}/venv'])

    # Use the direct path to the activate script
    venv_activate_script = f'{path}/venv/bin/activate'

    # Run the activate script as a separate process using zsh
    subprocess.run(['zsh', '-c', f'source {venv_activate_script}'])

def start_project():
    path = entry_path.get()
    subprocess.run(['code', f'{path}/app.py'])

# Create the main window
window = tk.Tk()
window.title("Project Setup")

# Create a label and entry for the directory path
label_path = ttk.Label(window, text="Enter Directory Path:")
label_path.pack()
entry_path = ttk.Entry(window)
entry_path.pack()

# Create buttons for directory creation, virtual environment setup, and starting the project
create_button = ttk.Button(window, text="Create Directory", command=create_directory)
setup_button = ttk.Button(window, text="Setup Virtual Environment", command=setup_virtualenv)
start_button = ttk.Button(window, text="Start Project", command=start_project)

create_button.pack()
setup_button.pack()
start_button.pack()

# Start the Tkinter event loop
window.mainloop()
