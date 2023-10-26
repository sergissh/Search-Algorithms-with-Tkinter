import tkinter as tk

from header import Header
from body import Body
class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Search Algorithms Tool')
        self.root.geometry("1200x800")
        self.root.config(bg="lightblue")
        self.root.resizable(width=0, height=0)

        self.header = Header(self.root)
        self.body = Body(self.root)
        self.root.mainloop()
        


app = Application()


