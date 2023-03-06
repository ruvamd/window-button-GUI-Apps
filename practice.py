import tkinter as tk
import os
import sys
from tkinter import filedialog
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
        # Get path from user
        path = filedialog.askopenfilename()

        # Add new button
        if path:
            button = tk.Button(self.master, text=path, command=lambda: self.run_application(path))
            button.pack(side=tk.TOP, fill=tk.X)
            self.buttons.append(button)

    def remove_button(self):
        # Remove last button
        if self.buttons:
            button = self.buttons.pop()
            button.pack_forget()
            button.destroy()

    def run_application(self, path):
        # Run application
        if path:
            if sys.platform.startswith('darwin'):
                os.system(f'open "{path}"')
            elif os.name == 'nt':
                os.startfile(path)
            elif os.name == 'posix':
                os.system(f'xdg-open "{path}"')

    def edit_button(self, button):
        # Get new label for button
        new_label = tk.simpledialog.askstring("Edit button", "Enter new label for button")

        # Update button label
        if new_label:
            button.config(text=new_label)

    def bind_events(self, button):
        # Bind right-click event to edit button
        button.bind("<Button-3>", lambda event, button=button: self.edit_button(button))

    # Bind events for all buttons
    def bind_all_events(self):
        for button in self.buttons:
            self.bind_events(button)


# Create main window
root = tk.Tk()
root.title("Button Window")

# Create button window
button_window = ButtonWindow(root)
button_window.pack()

# Bind events for all buttons
button_window.bind_all_events()

# Start application
root.mainloop()
