import networkx as nx

def is_valid_network(G, T):
    """
    Checks whether T is a valid network of G.
    Args:
        G: networkx.Graph
        T: networkx.Graph

    Returns:
        bool: whether T is a valid network
    """

    return nx.is_tree(T) and nx.is_dominating_set(G, T.nodes)


def average_pairwise_distance(T):
    """
    Computes the average pairwise distance between vertices in T.
    This is what we want to minimize!

    Args:
        T: networkx.Graph, a tree

    Returns:
        double: the average pairwise distance
    """
    path_lengths = nx.all_pairs_dijkstra_path_length(T)
    total_pairwise_distance = sum([sum(length[1].values()) for length in path_lengths]) / 2
    return total_pairwise_distance / (len(T) * (len(T) - 1))
