import tkinter as tk
import tkinter.filedialog
import tkinter.simpledialog
import os
import pathlib

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

    def run_application(self, button):
        # Run application
        os.startfile(button.file_path)

# Create main window
root = tk.Tk()
root.title("Button Window")

# Create button window
button_window = ButtonWindow(root)
button_window.pack()

# Start application
root.mainloop()
