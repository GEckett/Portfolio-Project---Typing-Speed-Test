import tkinter as tk
from tkinter import messagebox
from phrases import phrases
import random
import time


class TypeSpeedTestApp:
    def __init__(self, root):
        # Main App Variables
        self.test_phrase = "Phrase to type appears here."
        self.stopwatch = 0
        self.start_time = None
        self.type_speed = 0
        self.phrases = phrases
        self.paused = False

        # App appearance
        self.root = root
        self.root.title("Typing Speed Tester")

        self.title_label = tk.Label(self.root, text="Start test to get your Typing Speed.",
                                    font=("Helvetica", 16, "bold"))
        self.title_label.pack()

        self.phrase_label = tk.Label(self.root, text="Phrase to type appears here.",
                                    font=("Helvetica", 12, "bold"), pady=10)
        self.phrase_label.pack()

        self.test_frame = tk.Frame(self.root)
        self.test_frame.pack(pady=10)

        self.test_text = tk.Label(self.test_frame, text=f"Timer: {self.stopwatch:.2f} seconds")
        self.test_text.grid(row=0, column=1, padx=10)

        self.test_button = tk.Button(self.test_frame, text="Start Test", compound=tk.TOP, command=self.test)
        self.test_button.grid(row=1, column=0, padx=10)

        self.reset_button = tk.Button(self.test_frame, text="Reset", compound=tk.TOP, command=self.reset)
        self.reset_button.grid(row=2, column=0, padx=10)

        self.test_entry = tk.Entry(self.test_frame,width=100)
        self.test_entry.grid(row=1, column=1, padx=10)

    def reset(self):
        self.reset_timer()
        self.title_label.config(text="Start test to get your Typing Speed.")
        self.phrase_label.config(text="Phrase to type appears here.")
        self.test_entry.delete(0, tk.END)

    def test(self):
        self.title_label.config(text="")
        self.choose_phrase()
        self.start_timer()

    def choose_phrase(self):
        self.phrase_label.config(text=random.choice(self.phrases))

    def update_timer_label(self):
        if not self.paused:
            elapsed_time = time.time() - self.start_time
            self.stopwatch = elapsed_time
            self.test_text.config(text=f"Timer: {self.stopwatch:.2f} seconds")
            self.toggle_pause()
            self.root.update()

            # Schedule the next update after 100 milliseconds (adjust as needed)
            self.root.after(100, self.update_timer_label)
        else:
            print("Timer paused.")
            self.calculate_type_speed()

    def start_timer(self):
        self.start_time = time.time()
        self.paused = False

        # Start the automatic timer update
        self.update_timer_label()

    def reset_timer(self):
        # Stop the timer and reset the label
        self.start_time = None
        self.stopwatch = 0
        self.test_text.config(text="Timer: 0.00 seconds")

    def toggle_pause(self):
        # Toggle the pause state if the label and entry texts match
        label_text = self.phrase_label.cget("text")
        entry_text = self.test_entry.get()

        if label_text == entry_text:
            self.paused = not self.paused
            if self.paused:
                print("Timer paused.")
            else:
                print("Timer resumed.")
                # Restart the timer update if unpaused
                self.update_timer_label()
        else:
            pass

    def calculate_type_speed(self):
        phrase_chars = len(self.test_phrase)
        time_to_type = self.stopwatch
        chars_per_sec = phrase_chars/time_to_type
        self.type_speed = round(chars_per_sec * 60)
        self.title_label.config(text=f"Your typing speed is {self.type_speed} characters per minute.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypeSpeedTestApp(root)

    root.mainloop()
