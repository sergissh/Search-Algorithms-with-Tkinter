import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning
from PIL import Image, ImageTk
from body import Body
class Header(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.header_width = 230
        self.master = master
        self.configure(width=self.header_width, relief="solid", bg="yellow")
        self.place(x=0, y=0, relheight=1, width=self.header_width)
        self.initializeGraphSection()
        self.addHorizontalSeparator()

        self.initializeNodesSection()
        self.addHorizontalSeparator()

        self.initalizeAlgorithmsSection()
        self.addHorizontalSeparator()


        self.initializeSaveSection()
        self.addHorizontalSeparator()

        #Create Canvas border
        border_canvas = tk.Canvas(self, width=2, bg="black", bd=0, highlightthickness=0)
        border_canvas.place(x=self.header_width-1, y=0, relheight=1)

    def addHorizontalSeparator(self):
        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x')

    def initializeGraphSection(self):
        
        def checkboxAction():
            body = section1.master.master.body
            if boolCheck1.get() == 1:
                body.displayDistances(True)
            else:
                body.displayDistances(False)
        #Section 1
        section1 = tk.Frame(self, width=self.winfo_screenmmwidth(), pady=10)
        section1.pack(fill=tk.X)

        # Add empty columns on both sides to center the items
        section1.grid_columnconfigure(0, weight=1)
        section1.grid_columnconfigure(3, weight=1)


        # Create a label and center it in the frame
        label = tk.Label(section1, text="Initialize Graph", font=('Helvetica', 10, 'bold'))
        label.grid(row=0, column=1, columnspan=2, sticky=tk.N + tk.E + tk.W + tk.S)

        # Create the first button and center it in the frame
        button1 = tk.Button(section1, text="Create Graph", padx=8, pady=6, command=self.createNewGraph)
        button1.grid(row=1, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

        # Create the second button and center it in the frame
        button2 = tk.Button(section1, text="Load Graph", padx=8, pady=6)
        button2.grid(row=1, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)
        
        # Create the display distances checkbox in the frame
        boolCheck1 = tk.IntVar()
        checkbox = tk.Checkbutton(section1, text="Disp. Distances", padx=8, pady=6, variable=boolCheck1, font=('Helvetica', 8), command=checkboxAction)
        checkbox.grid(row=2, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

    def initializeNodesSection(self):
        #Section 2
        section2 = tk.Frame(self, width=self.winfo_screenmmwidth(), pady=10)
        section2.pack(fill=tk.X)

        # Add empty columns on both sides to center the items
        section2.grid_columnconfigure(0, weight=1)
        section2.grid_columnconfigure(3, weight=1)

        # Create a label and center it in the frame
        label = tk.Label(section2, text="Set Start", font=('Helvetica', 10, 'bold'))
        label.grid(row=0, column=1, columnspan=2, sticky=tk.N + tk.E + tk.W + tk.S)

        # Create the first button and center it in the frame
        button1 = tk.Button(section2, text="Set Start", padx=8, pady=6)
        button1.grid(row=1, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

        # Create the second button and center it in the frame
        button2 = tk.Button(section2, text="Generate Visits", padx=8, pady=6)
        button2.grid(row=1, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

        # Create the third button and center it in the frame
        button3 = tk.Button(section2, text="Load Visits", padx=8, pady=6)
        button3.grid(row=2, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)


    def initalizeAlgorithmsSection(self):
        #Section 3
        section3 = tk.Frame(self, width=self.winfo_screenmmwidth(), pady=10)
        section3.pack(fill=tk.X)

        # Add empty columns on both sides to center the items
        section3.grid_columnconfigure(0, weight=1)
        section3.grid_columnconfigure(3, weight=1)

        # Create a label and center it in the frame
        label = tk.Label(section3, text="Search Algorithms", font=('Helvetica', 10, 'bold'))
        label.grid(row=0, column=1, columnspan=2, sticky=tk.N + tk.E + tk.W + tk.S)

        # Create the first button and center it in the frame
        button1 = tk.Button(section3, text="BFS", padx=8, pady=6)
        button1.grid(row=1, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

        # Create the secons button and center it in the frame
        button2 = tk.Button(section3, text="DFS", padx=8, pady=6)
        button2.grid(row=1, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

        # Create the third button and center it in the frame
        button2 = tk.Button(section3, text="Greedy", padx=8, pady=6)
        button2.grid(row=2, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

        # Create the fourth button and center it in the frame
        button2 = tk.Button(section3, text="Dijkstra", padx=8, pady=6)
        button2.grid(row=2, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

    def initializeSaveSection(self):
        #Section 4
        section4 = tk.Frame(self, width=self.winfo_screenmmwidth(), pady=10)
        section4.pack(fill=tk.X)

        # Add empty columns on both sides to center the items
        section4.grid_columnconfigure(0, weight=1)
        section4.grid_columnconfigure(3, weight=1)

        # Create a label and center it in the frame
        label = tk.Label(section4, text="Save Graph", font=('Helvetica', 10, 'bold'))
        label.grid(row=0, column=1, columnspan=2, sticky=tk.N + tk.E + tk.W + tk.S)

        # Create the first button and center it in the frame
        button1 = tk.Button(section4, text="Save Graph", padx=8, pady=6)
        button1.grid(row=1, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

        # Create the secons button and center it in the frame
        button2 = tk.Button(section4, text="Save Visits", padx=8, pady=6)
        button2.grid(row=1, column=2, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

        # Create the third button and center it in the frame
        button2 = tk.Button(section4, text="Save Results", padx=8, pady=6)
        button2.grid(row=2, column=1, sticky=tk.N + tk.E + tk.W + tk.S, padx=10, pady=10)

    def createNewGraph(self):

        def checkGraph():
            body = newWindow.master.master.body
            nodes = entry1.get()
            edges = entry2.get()
            if not nodes.isdigit() or not edges.isdigit():
                showwarning(title="Error", message="Enter an Integer")
            elif int(nodes) <= 1:
                showwarning(title="Error", message="Nodes must be higher than 1")
            elif int(edges) < int(nodes) - 1:
                showwarning(title="Error", message="Number of Edges must me higher")
            else:
                body.createGraph(int(nodes), int(edges))
                newWindow.destroy()

        # Create new Window
        newWindow = tk.Toplevel(self)
        newWindow.title("Create Graph")
        newWindow.geometry("250x160")
        newWindow.resizable(width=0, height=0)
        
        # Create widgets
        label1 = tk.Label(newWindow, text="Nº of Nodes:")
        label2 = tk.Label(newWindow, text="Nº of Edges:")
        button1 = tk.Button(newWindow, text="Accept", padx=8, pady=6, command=checkGraph)
        button2 = tk.Button(newWindow, text="Cancel", padx=8, pady=6, command=newWindow.destroy)
        entry1 = tk.Entry(newWindow)
        entry1.insert(0, 10)
        entry1.place(x=90, y=20)
        entry2 = tk.Entry(newWindow)
        entry2.insert(0, 20)
        entry2.place(x=90, y=60)

        # Place Widgets
        label1.place(x=15, y=20)
        label2.place(x=15, y=60)
        button1.place(x=25, y=110)
        button2.place(x=165, y=110)
        
        

        