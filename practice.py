import tkinter as tk
import os

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

        # Create four custom buttons
        for i in range(4):
            button_frame = tk.Frame(self.master)
            button_frame.pack(side=tk.TOP, fill=tk.X)

            # Path entry
            path_entry = tk.Entry(button_frame)
            path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

            # Run button
            run_button = tk.Button(button_frame, text=f"Button {i+1}", command=lambda index=i: self.run_application(path_entry.get()))
            run_button.pack(side=tk.LEFT)

            self.buttons.append(button_frame)

    def add_button(self):
        # Add new button
        button_frame = tk.Frame(self.master)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        # Path entry
        path_entry = tk.Entry(button_frame)
        path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Run button
        run_button = tk.Button(button_frame, text="New Button", command=lambda: self.run_application(path_entry.get()))
        run_button.pack(side=tk.LEFT)

        self.buttons.append(button_frame)

    def remove_button(self):
        # Remove last button
        if self.buttons:
            button_frame = self.buttons.pop()
            button_frame.pack_forget()
            button_frame.destroy()

    def run_application(self, path):
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
