import tkinter as tk
from tkinter import messagebox
import time


class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("My Pomodoro")

        self.work_time = 25 * 60
        self.break_time = 5 * 60
        self.time_left = self.work_time
        self.is_work = True
        self.running = False
        self.completed_sessions = 0

        # GUI Setup
        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.status_label = tk.Label(root, text="Work Session", font=("Helvetica", 14))
        self.status_label.pack()

        self.counter_label = tk.Label(root, text="Completed: 0", font=("Helvetica", 12))
        self.counter_label.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.toggle_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update_display()

    def toggle_timer(self):
        self.running = not self.running
        self.start_button.config(text="Pause" if self.running else "Resume")
        if self.running:
            self.countdown()

    def countdown(self):
        if self.running and self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        elif self.running:
            self.session_complete()

    def session_complete(self):
        self.running = False
        self.start_button.config(text="Start")
        self.is_work = not self.is_work

        if self.is_work:
            self.completed_sessions += 1
            messagebox.showinfo("Session Complete", "Time for a break!")
            self.time_left = self.break_time
        else:
            messagebox.showinfo("Break Over", "Time to work!")
            self.time_left = self.work_time

        self.update_display()
        self.counter_label.config(text=f"Completed: {self.completed_sessions}")

    def reset_timer(self):
        self.running = False
        self.time_left = self.work_time
        self.is_work = True
        self.completed_sessions = 0
        self.start_button.config(text="Start")
        self.update_display()
        self.counter_label.config(text="Completed: 0")

    def update_display(self):
        mins, secs = divmod(self.time_left, 60)
        self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
        status_text = "Work Session" if self.is_work else "Break Time"
        self.status_label.config(text=status_text)
        color = "#FF6961" if self.is_work else "#77DD77"  # Red/Green colors
        self.timer_label.config(fg=color)
        self.status_label.config(fg=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()