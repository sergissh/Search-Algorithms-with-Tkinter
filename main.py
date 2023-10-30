import tkinter as tk

from header import Header
from body import Body
class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Search Algorithms Tool')
        self.geometry("1200x800")
        self.resizable(width=0, height=0)
        self.header = Header(self)
        self.body = Body(self)

app = Application()
app.mainloop()


