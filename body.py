import tkinter as tk
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


from graph import Graph


class Body(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.body_width = 970
        self.configure(width=self.body_width)
        self.place(x=231, y=0, relheight=1)
        self.graph = None
        self.fontAnnotations = 11

    def createGraph(self, num_nodes, num_edges):
        self.graph = Graph(num_nodes=num_nodes, num_edges=num_edges)
        self.displayGraph()
        self.canvas_widget.bind("<MouseWheel>", self.zoom)
        self.canvas_widget.bind("<ButtonPress-1>", self.on_mouse_press)
        self.canvas_widget.bind("<B1-Motion>", self.on_mouse_drag)

    def displayGraph(self):
        # Layout the graph
        self.pos = nx.spring_layout(self.graph.graph)

        # Create a Matplotlib figure and plot the network graph
        self.fig, self.ax = plt.subplots()
        nx.draw(self.graph.graph, self.pos, with_labels=True, ax=self.ax, labels=self.graph.node_labels)

        # Create a FigureCanvasTkAgg widget to display the graph in the tkinter frame
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.place(x= 0, y=0, width=self.body_width, relheight=1)
        
    
    def displayDistances(self, checkbox):
        if checkbox:
            edge_labels = {(u, v): self.graph.graph[u][v]['weight'] for u, v in self.graph.graph.edges()}
            distance = .01
            zoom_factor = 0.8
            for edge, label in edge_labels.items():
                x1, y1 = self.pos[edge[0]]
                x2, y2 = self.pos[edge[1]]
                x = (x1 + x2) / 2
                y = (y1 + y2) / 2
                dx = x2 - x1
                dy = y2 - y1

                # **0.5 == sqrt()
                length = (dx**2 + dy**2)**0.5
                x_par = x + (distance / length) * dy
                y_par = y + (distance / length) * dx
                fontSize = self.fontAnnotations * zoom_factor
                plt.annotate(label, (x_par, y_par), fontsize=fontSize, ha="center", va='center', backgroundcolor="w")
            self.canvas.draw()
        else:
            for text in self.ax.texts:
                if text.get_text() not in self.graph.node_labels.values():
                    text.remove()
            self.canvas.draw()

    def zoom(self, event):
        zoom_factor = 0.8
        x, y = event.x, event.y
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        xdata = xlim[0] + (xlim[1] - xlim[0]) * x / self.canvas_widget.winfo_width()
        ydata = ylim[0] + (ylim[1] - ylim[0]) * (1 - y / self.canvas_widget.winfo_height())
        if event.delta > 0:
            self.ax.set_xlim(xdata - (xdata - xlim[0]) * zoom_factor, xdata + (xlim[1] - xdata) * zoom_factor)
            self.ax.set_ylim(ydata - (ydata - ylim[0]) * zoom_factor, ydata + (ylim[1] - ydata) * zoom_factor)

        elif event.delta < 0:
            self.ax.set_xlim(xdata - (xdata - xlim[0]) / zoom_factor, xdata + (xlim[1] - xdata) / zoom_factor)
            self.ax.set_ylim(ydata - (ydata - ylim[0]) / zoom_factor, ydata + (ylim[1] - ydata) / zoom_factor)
        
        newFontSize = self.fontAnnotations * zoom_factor
        for text in self.ax.texts:
            text.set_fontsize(newFontSize)
        
        self.canvas.draw()

    def on_mouse_press(self, event):
        self.start_x, self.start_y = event.x, event.y

    def on_mouse_drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.start_x, self.start_y = event.x, event.y
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        x_range = xlim[1] - xlim[0]
        y_range = ylim[1] - ylim[0]
        x_scale = x_range / self.canvas_widget.winfo_width()
        y_scale = y_range / self.canvas_widget.winfo_height()
        self.ax.set_xlim(xlim[0] - dx * x_scale, xlim[1] - dx * x_scale)
        self.ax.set_ylim(ylim[0] + dy * y_scale, ylim[1] + dy * y_scale)
        self.canvas.draw()
