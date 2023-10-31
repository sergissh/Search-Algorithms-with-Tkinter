import tkinter as tk
from tkinter import ttk
import networkx as nx
import random
from networkx.generators.random_graphs import erdos_renyi_graph
from networkx.drawing.nx_agraph import graphviz_layout
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class Graph():
    def __init__(self, num_nodes, num_edges):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.p = 0.5
        while True:
            self.graph = nx.gnm_random_graph(num_nodes, num_edges)
            for u, v in self.graph.edges():
                self.graph[u][v]['weight'] = random.randint(1, 10)  
            #check for isolated nodes
            isolated_nodes = [node for node in self.graph.nodes() if self.graph.degree(node) == 0]
            if not isolated_nodes:
                self.node_labels = {node: f"V{node}" for node in self.graph.nodes()}
                print(self.node_labels)
                break

        