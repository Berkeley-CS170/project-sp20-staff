import numpy as numpy
import networkx as nx
import os

# Set path to cwd; make in/ and out/ dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))
if not os.path.exists('in'): os.mkdir('in')
if not os.path.exists('out'): os.mkdir('out')

def parse_input_file(file):
    with open(file, 'r') as fo:
        n = int(fo.readline())
        lines = fo.read().splitlines()
        fo.close()
        G = nx.parse_edgelist(lines, nodetype = int, data=(('weight', float),))
        G.add_nodes_from(range(n))
        return G

def write_input_file(G, file):
    with open(file, 'w') as fo:
        n = len(G)
        lines = nx.generate_edgelist(G, data=['weight'])
        fo.write(str(n) + '\n')
        fo.writelines('\n'.join(lines))
        fo.close()

def read_output_file(file):
    with open(file, 'r') as fo: 
        nodes = fo.readline()
        lines = fo.read().splitlines()
        fo.close()
        T = nx.parse_edgelist(lines, nodetype = int, data=(('weight', float),))
        T.add_nodes_from(map(int, nodes.split()))
        return T

def write_output_file(T, file):
    with open(file, 'w') as fo: 
        fo.write(' '.join(map(str, T.nodes)) + '\n')
        lines = nx.generate_edgelist(T, data=['weight'])
        fo.writelines('\n'.join(lines))
        fo.close()

G = parse_input_file('in/test.in')
T = nx.minimum_spanning_tree(G)
# T.remove_edge(0, 1)
T.remove_node(0)
write_output_file(T, 'out/test.out')
T = read_output_file('out/test.out')
print(T.nodes)

# G = nx.Graph()
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_edge(2, 3)    
# nx.write_weighted_edgelist(G, test)
