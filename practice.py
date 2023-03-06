import tkinter as tk
import tkinter.filedialog
import tkinter.simpledialog
import subprocess
import pathlib
import os
import sys

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

        # Add pencil sign button
        pencil_sign_button = tk.Button(buttons_frame, text="\u270E", command=self.rename_button)
        pencil_sign_button.pack(side=tk.LEFT)

        # Add add button
        add_button = tk.Button(buttons_frame, text="+", command=self.add_button)
        add_button.pack(side=tk.RIGHT)

        # Add remove button
        remove_button = tk.Button(buttons_frame, text="-", command=self.remove_button)
        remove_button.pack(side=tk.RIGHT)

    def add_button(self):
        # Get path for new button
        path = tk.filedialog.askopenfilename()

        if path:
            # Add new button
            button = tk.Button(self.master, text=pathlib.Path(path).name, command=lambda: self.run_application(button))
            button.file_path = path
            button.pack(side=tk.TOP, fill=tk.X)
            self.buttons.append(button)

    def remove_button(self):
        # Remove last button
        if self.buttons:
            button = self.buttons.pop()
            button.pack_forget()
            button.destroy()

    def rename_button(self):
        # Select button to rename
        if self.buttons:
            button = tkinter.simpledialog.askinteger("Rename Button", "Enter button index to rename (starting from 1):")
            if button and button > 0 and button <= len(self.buttons):
                new_name = tkinter.simpledialog.askstring("Rename Button", "Enter new name:")
                if new_name:
                    self.buttons[button-1].config(text=new_name)

    def run_application(self, button):
        # Run application
        if sys.platform.startswith('darwin'):  # For macOS
            subprocess.call(('open', button.file_path))
        elif os.name == 'nt':  # For Windows
            os.startfile(button.file_path)
        elif os.name == 'posix':  # For Linux, Unix, etc.
            subprocess.call(('xdg-open', button.file_path))

# Create main window
root = tk.Tk()
root.title("Button Window")

# Create button window
button_window = ButtonWindow(root)
button_window.pack()

# Start application
root.mainloop()
