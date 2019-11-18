# Installation

```bash
# Sagemath
# Attention: uniquement disponible sur Debian >= 9 ou ubuntu >= 18.4
sudo apt install sagemath
# Sinon voir: https://doc.sagemath.org/html/en/installation/

# Networkx
pip3 install networkx
```

# Exécution

```bash
# Exporter les images de tous les graphes à 5 sommets dans le dossier graph5
python3 g6_to_image.py

# Filtrer les graphes à 5 sommets et exporter les images dans le dossier graph5_filtered
sage filter_graphs.py 5
```

# Documentation

Sage:
- [Graph theory](http://doc.sagemath.org/html/en/reference/graphs/index.html)
- [Common graphs](http://doc.sagemath.org/html/en/reference/graphs/sage/graphs/graph_generators.html)
