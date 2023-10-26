import tkinter as tk
from tkinter import ttk
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

        #Function that validates that the input is a number
        def onValidate(P, entry):
            if not validate_input(P):
                entry.set("".join(filter(str.isdigit(), P)))
        def validate_input(P):
            if P == "":
                return True
            if P.isdigit():
                return True
            else:
                return False
        #Obtain entry values of Esges and Nodes, when submitting the form
        def getNodesEdges():
            entry1.get()
            entry2.get()

        # Create new Window
        newWindow = tk.Toplevel(self.master)
        newWindow.title("Create Graph")
        newWindow.geometry("250x150")
        newWindow.resizable(width=0, height=0)

        #Create a validation function for the entries
        validate = newWindow.register(validate_input)

        # Create widgets
        label1 = tk.Label(newWindow, text="Nº of Nodes:")
        label2 = tk.Label(newWindow, text="Nº of Edges:")
        entry1 = tk.Entry(newWindow, width=10, validate="key", validatecommand=(validate, "%P", entry1))
        entry2 = tk.Entry(newWindow, width=10, validate="key", validatecommand=(validate, "%P", entry2))
        button = tk.Button(newWindow, text="Create Graph", padx=8, pady=6, command=getNodesEdges)

        # Place Widgets
        label1.place(x=15, y=20)
        label2.place(x=15, y=60)
        entry1.place(x=90, y=20)
        entry2.place(x=90, y=60)
        button.place(relx=.5, y=120, anchor="center")
        
        
        

        