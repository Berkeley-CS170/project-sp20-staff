import networkx as nx
from parse import read_input_file, write_output_file 
import sys

def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """

    T =  # TODO: your code here!
    return nx.minimum_spanning_tree(G)



if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G = read_input_file(path)
    T = solve(G)
    write_output_file(T, 'out/test.out')