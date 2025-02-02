import tkinter as tk
import random
import ctypes
import subprocess
import os

# Minimize the command prompt window
def minimize_console():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')

    SW_MINIMIZE = 6

    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, SW_MINIMIZE)

class CatchMeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch Me If You Can!")
        self.label = tk.Label(root, text="Try to catch me!", font=("Helvetica", 16), bg="yellow")
        self.label.pack()
        self.label.bind("<Enter>", self.move_label)
        self.root.geometry("200x100")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.place_window_randomly()

    def move_label(self, event):
        x = random.randint(0, self.root.winfo_width() - self.label.winfo_width())
        y = random.randint(0, self.root.winfo_height() - self.label.winfo_height())
        self.label.place(x=x, y=y)

    def on_closing(self):
        self.root.destroy()
        self.restart_app()

    def restart_app(self):
        new_root = tk.Tk()
        CatchMeApp(new_root)
        new_root.mainloop()

    def place_window_randomly(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = random.randint(0, screen_width - 200)  # Subtract window width
        y = random.randint(0, screen_height - 100)  # Subtract window height
        self.root.geometry(f"200x100+{x}+{y}")

if __name__ == "__main__":
    minimize_console()
    root = tk.Tk()
    app = CatchMeApp(root)
    root.mainloop()
