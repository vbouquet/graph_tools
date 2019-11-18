import sys
import os
import networkx as nx
import matplotlib.pyplot as plt

from shutil import rmtree

def save_all_graphs(file, output):
    with open(file, "r") as f:
        for i, line in enumerate(f, 1):
            print(line)
            G = nx.from_graph6_bytes(line[:-1].encode())
            nx.draw(G)
            fig_path = os.path.join(output, str(i))
            plt.savefig(fig_path)
            plt.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError(
            "Nombre de sommets necessaires a passer en argument 1"
        )
    file = os.path.join("input", "graph%s.g6" % sys.argv[1])
    output = "graph%s" %sys.argv[1]
    try:
        rmtree(output)
    except OSError:
        print("Le dossier %s n existe pas" % output)
    os.mkdir(output)

    save_all_graphs(file, output)
