import tkinter as tk
import tkinter.filedialog
import tkinter.simpledialog
import subprocess
import pathlib
import os
import sys
import json

class ButtonWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.buttons = []
        self.create_widgets()
        self.load_buttons()

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
            button = tk.Button(self.master, text=pathlib.Path(path).name, command=lambda path=path: self.run_application(path))
            button.file_path = path
            button.pack(side=tk.TOP, fill=tk.X)
            self.buttons.append(button)
            self.save_buttons()


    def remove_button(self):
        # Remove last button
        if self.buttons:
            button = self.buttons.pop()
            button.pack_forget()
            button.destroy()
            self.save_buttons()

    def rename_button(self):
        # Select button to rename
        if self.buttons:
            button = tkinter.simpledialog.askinteger("Rename Button", "Enter button index to rename (starting from 1):")
            if button and button > 0 and button <= len(self.buttons):
                new_name = tkinter.simpledialog.askstring("Rename Button", "Enter new name:")
                if new_name:
                    self.buttons[button-1].config(text=new_name)
                    self.save_buttons()

    def run_application(self, path):
        # Run application
        if sys.platform.startswith('darwin'):  # For macOS
            subprocess.call(('open', path))
        elif os.name == 'nt':  # For Windows
            os.startfile(path)
        elif os.name == 'posix':  # For Linux, Unix, etc.
            subprocess.call(('xdg-open', path))

    def save_buttons(self):
        # Save button data to file
        data = [{'name': button['text'], 'path': button.file_path} for button in self.buttons]
        with open('buttons.json', 'w') as f:
            json.dump(data, f)

    def load_buttons(self):
        # Load button data from file
        try:
            with open('buttons.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    button = tk.Button(self.master, text=item['name'], command=lambda path=item['path']: self.run_application(path))
                    button.file_path = item['path']
                    button.pack(side=tk.TOP, fill=tk.X)
                    self.buttons.append(button)
                    
        except FileNotFoundError:
            pass
        
# Create main window
root = tk.Tk()
root.title("Button Window")

# Create button window
button_window = ButtonWindow(root)
button_window.pack()

# Start application
root.mainloop()
