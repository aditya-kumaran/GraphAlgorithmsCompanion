"""
Floyd-Warshall Algorithm Implementation

This module contains the Floyd-Warshall algorithm for finding all-pairs shortest paths.
The function returns a dictionary with visualization-friendly results.
"""

import networkx as nx
from typing import Dict, Any, Tuple, List

def floyd_warshall_algorithm(graph: nx.Graph) -> Dict[str, Any]:
    """
    Perform the Floyd-Warshall algorithm on the given graph.
    
    Args:
        graph: NetworkX graph object (can be directed or undirected)
    
    Returns:
        Dictionary containing:
        - 'distance': dict-of-dict with shortest distances between all pairs
        - 'next_node': dict-of-dict used to reconstruct the shortest paths
        - 'shortest_paths': dict-of-dict with reconstructed paths between all pairs
        - 'infinite_pairs': List of (u, v) pairs where no path exists
    """
    nodes = list(graph.nodes())
    dist = {u: {v: float("inf") for v in nodes} for u in nodes}
    next_node = {u: {v: None for v in nodes} for u in nodes}
    
    for u in nodes:
        dist[u][u] = 0
        for v in graph.neighbors(u):
            w = graph[u][v].get("weight", 1.0)
            dist[u][v] = w
            next_node[u][v] = v

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
    
    # Reconstruct paths
    shortest_paths = {}
    infinite_pairs = []

    for u in nodes:
        shortest_paths[u] = {}
        for v in nodes:
            if next_node[u][v] is None and u != v:
                shortest_paths[u][v] = []
                infinite_pairs.append((u, v))
            else:
                shortest_paths[u][v] = _reconstruct_path(u, v, next_node)
    
    return {
        'distance': dist,
        'next_node': next_node,
        'shortest_paths': shortest_paths,
        'infinite_pairs': infinite_pairs
    }


def _reconstruct_path(u: Any, v: Any, next_node: Dict[Any, Dict[Any, Any]]) -> List[Any]:
    """
    Helper to reconstruct the shortest path from u to v using the next_node matrix.
    
    Args:
        u: Start node
        v: End node
        next_node: Matrix of next hops from Floyd-Warshall
    
    Returns:
        List of nodes in the shortest path from u to v
    """
    if next_node[u][v] is None:
        return []
    
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    
    return path
