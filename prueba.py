import tkinter as tk
from tkinter import X, Y, BOTTOM, RIGHT, LEFT, Y, HORIZONTAL
class TextExample(tk.Frame):
    def __init__(self, master=None):
        super().__init__()

        sy = tk.Scrollbar(self)
        sx = tk.Scrollbar(self,  orient=HORIZONTAL)
        editor = tk.Text(self, height=500, width=300, wrap='none')
        sx.pack(side=BOTTOM, fill=X)
        sy.pack(side=RIGHT, fill=Y)
        editor.pack(side=LEFT, fill=Y)
        sy.config(command=editor.yview)
        sx.config(command=editor.xview)
        self.pack()
def main():
    root = tk.Tk()
    root.geometry("800x500+0+0")
    app = TextExample(master=root)
    root.mainloop()  
if __name__ == '__main__':
    main()
    