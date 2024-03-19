import tkinter as tk
from tkinter import filedialog, Text

class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Notepad")
        self.geometry("600x400")

        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)

        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Exit", command=self.quit)
        
        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

        self.text_widget = Text(self)
        self.text_widget.pack(expand=True, fill='both')

    def new_file(self):
        Notepad().mainloop()

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            with open(filename, 'r') as f:
                content = f.read()
                self.text_widget.delete('1.0', "end")
                self.text_widget.insert('1.0', content)

    def save_file(self):
        filename = filedialog.asksaveasfilename()
        if filename:
            with open(filename, 'w') as f:
                f.write(self.text_widget.get('1.0', 'end'))

if __name__ == "__main__":
    window = Notepad()
    window.mainloop()