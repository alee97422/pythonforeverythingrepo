import tkinter as tk
import sounddevice as sd
import numpy as np
import aubio

# Define the target frequencies for standard guitar tuning
target_frequencies = [82.41, 110.00, 146.83, 196.00, 246.94, 329.63]

# Set up audio stream
sample_rate = 44100
buffer_size = 1024

def update_tuning():
    # Convert input to mono
    indata_mono = np.mean(indata, axis=1)

    # Detect pitch
    pitch = pitch_o(indata_mono)[0]
    confidence = pitch_o.get_confidence()

    if confidence > 0.6:
        # Calculate closest target frequency
        closest_frequency = min(target_frequencies, key=lambda x: abs(x - pitch))

        # Calculate difference in cents
        cents = 1200 * np.log2(pitch / closest_frequency)

        # Determine tuning status
        if abs(cents) <= 10:
            status = "In Tune"
        elif cents < 0:
            status = "Flat"
        else:
            status = "Sharp"

        # Update GUI
        label_pitch.config(text=f"Detected Pitch: {pitch:.2f} Hz")
        label_status.config(text=f"Status: {status}")
        label_cents.config(text=f"Cents: {cents:.2f}")

def start_tuning():
    global stream
    stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate)
    stream.start()

def stop_tuning():
    stream.stop()

def audio_callback(indata, frames, time, status):
    update_tuning()

# Initialize Aubio pitch detection
tolerance = 0.8
pitch_o = aubio.pitch("default", buffer_size, buffer_size // 2, sample_rate)
pitch_o.set_tolerance(tolerance)

# Create the GUI
root = tk.Tk()
root.title("Guitar Tuner")

# Labels
label_pitch = tk.Label(root, text="Detected Pitch: ")
label_pitch.pack()
label_status = tk.Label(root, text="Status: ")
label_status.pack()
label_cents = tk.Label(root, text="Cents: ")
label_cents.pack()

# Buttons
start_button = tk.Button(root, text="Start Tuning", command=start_tuning)
start_button.pack()
stop_button = tk.Button(root, text="Stop Tuning", command=stop_tuning)
stop_button.pack()

root.mainloop()
