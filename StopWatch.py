import tkinter as tk
import time

class StopWatch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stopwatch")
        self.label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 24))
        self.label.pack()
        self.seconds = 0
        self.running = False
        self.button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.button.pack()
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.button.config(text="Pause")
            self.update_timer()
        else:
            self.running = True
            self.button.config(text="Pause")

    def pause_timer(self):
        if self.running:
            self.running = False
            self.button.config(text="Resume")
            self.after_cancel(self.timer_id)

    def reset_timer(self):
        self.running = False
        self.seconds = 0
        self.label.config(text="00:00:00")
        self.button.config(text="Start")

    def update_timer(self):
        if self.running:
            self.label.config(text=time.strftime("%M:%S", time.gmtime(self.seconds)) + ":" + str(self.seconds % 100).zfill(2))
            self.seconds += 1
            self.root.after(10, self.update_timer)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    stopwatch = StopWatch()
    stopwatch.run()