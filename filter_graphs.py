#!/usr/bin/env sage
import os
import sys

from shutil import rmtree
from sage.all import *
from sage.graphs.graph_input import from_graph6

if len(sys.argv) < 2:
    raise ValueError(
        "Nombre de sommets necessaires a passer en argument 1"
    )

n = int(sys.argv[1])
file = os.path.join("input", "graph%d.g6" % n)
output = "graph%d_filtered" % n

P7 = graphs.PathGraph(7)

claw = graphs.ClawGraph()
K4 = graphs.CompleteGraph(4)
diamond = graphs.DiamondGraph()
C4 = graphs.CycleGraph(4)
C5 = graphs.CycleGraph(5)
C6 = graphs.CycleGraph(6)
C7 = graphs.CycleGraph(7)
C8 = graphs.CycleGraph(8)
C9 = graphs.CycleGraph(9)
butterfly = graphs.ButterflyGraph()
list_forbidden_graphs = [claw, K4, diamond, C4, C5, C6, C7, C8, C9, butterfly]
Kn = Graph(n)

try:
    rmtree(output)
except OSError:
    print("Le dossier %s n existe pas" % output)
os.mkdir(output)

with open(file, "r") as f:
    for i, line in enumerate(f, 1):
        G = Graph()
        from_graph6(G, line[:-1])

        if G.is_isomorphic(Kn):
            continue

        if P7.subgraph_search(G, induced=True):
            continue

        save = True
        for H in list_forbidden_graphs:
            if G.subgraph_search(H, induced=True):
                save = False
                break

        if save:
            p = G.plot()
            p_path = os.path.join(output, "%d.png" % i)
            p.save(p_path)