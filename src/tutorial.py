# Import modul
import networkx as nx
import matplotlib.pyplot as plt

# Import fungsi yang sudah dibuat
from typing import List, Tuple

# Inisialisasi daftar edge (hubungan antar node)
edges: List[Tuple[int, int]] = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]

# Buat graf dari daftar edge
G = create_graph(edges)

# 1. Cek derajat (degree) suatu node
node = 4
print(f"Degree dari node {node}: {get_degree(G, node)}")

# 2. Lakukan traversal DFS dari node 1
print(f"DFS Traversal dari node 1: {dfs_traversal(G, 1)}")

# 3. Lakukan traversal BFS dari node 1
print(f"BFS Traversal dari node 1: {bfs_traversal(G, 1)}")

# 4. Cari jalur terpendek dari node 1 ke node 5
source, target = 1, 5
print(f"Jalur terpendek dari {source} ke {target}: {find_shortest_path(G, source, target)}")

# 5. Visualisasi graf
visualize_graph(G)
