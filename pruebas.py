import tkinter as tk
from tkinter import ttk
import networkx as nx
import random
from networkx.drawing.nx_agraph import graphviz_layout
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def create_and_show_network_graph():
    # Create a sample network graph
    G = nx.Graph()
    num_nodes = 10
    G.add_nodes_from(range(num_nodes))
    for u in G.nodes():
        for v in G.nodes():
            if u != v and not G.has_edge(u, v):
                distance = random.uniform(1.0, 10.0)
                G.add_edge(u, v, weight=distance)
    
    # Layout the graph
    pos = nx.spring_layout(G)    
    
    # Create a Matplotlib figure and plot the network graph
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, ax=ax)
    
    # Create a FigureCanvasTkAgg widget to display the graph in the tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    
    # Function to zoom in and out
    def on_mouse_wheel(event):
        zoom_factor = 0.8  # Adjust this value as needed
        x, y = event.x, event.y
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        xdata = xlim[0] + (xlim[1] - xlim[0]) * x / canvas_widget.winfo_width()
        ydata = ylim[0] + (ylim[1] - ylim[0]) * (1 - y / canvas_widget.winfo_height())
        if event.delta > 0:
            ax.set_xlim(xdata - (xdata - xlim[0]) * zoom_factor, xdata + (xlim[1] - xdata) * zoom_factor)
            ax.set_ylim(ydata - (ydata - ylim[0]) * zoom_factor, ydata + (ylim[1] - ydata) * zoom_factor)
        elif event.delta < 0:
            ax.set_xlim(xdata - (xdata - xlim[0]) / zoom_factor, xdata + (xlim[1] - xdata) / zoom_factor)
            ax.set_ylim(ydata - (ydata - ylim[0]) / zoom_factor, ydata + (ylim[1] - ydata) / zoom_factor)
        canvas.draw()
    
    canvas_widget.bind("<MouseWheel>", on_mouse_wheel)

root = tk.Tk()
root.title("Network Graph Display")

# Create a frame within the main window
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create and display the network graph with zooming
create_and_show_network_graph()

root.mainloop()