import tkinter as tk
from tkinter import ttk
import networkx as nx
import random
from networkx.drawing.nx_agraph import graphviz_layout
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Network Graph Display")
root.geometry("400x400")

# Create a frame within the main window
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create and display the network graph with zooming
image = Image.open("./app-images/alert.jpg")
image = image.resize((300, 300))
alert_image = ImageTk.PhotoImage(image)
alert_label = tk.Label(frame, image=alert_image).pack()

root.mainloop()