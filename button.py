import tkinter as tk
import tkinter.simpledialog as sd
import os
from pathlib import Path

class ButtonWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        # Create buttons frame
        buttons_frame = tk.Frame(self.master)
        buttons_frame.pack(side=tk.TOP, fill=tk.X)

        # Add button
        add_button = tk.Button(buttons_frame, text="+", command=self.add_button)
        add_button.pack(side=tk.RIGHT)

        # Remove button
        remove_button = tk.Button(buttons_frame, text="-", command=self.remove_button)
        remove_button.pack(side=tk.RIGHT)

    def add_button(self):
        # Get name for new button
        name = sd.askstring("Button Name", "Enter the name for the new button:")

        if name:
            # Add new button
            button = tk.Button(self.master, text=name, command=lambda: self.run_application(len(self.buttons)))
            button.pack(side=tk.TOP, fill=tk.X)
            self.buttons.append(button)

    def remove_button(self):
        # Remove last button
        if self.buttons:
            button = self.buttons.pop()
            button.pack_forget()
            button.destroy()

    def run_application(self, index):
        # Get path from user
        path = tk.filedialog.askopenfilename()

        # Run application
        if path:
            os.system(f'"{path}"')

# Create main window
root = tk.Tk()
root.title("Button Window")

# Create button window
button_window = ButtonWindow(root)
button_window.pack()

# Start application
root.mainloop()
