import numpy as numpy
import networkx as nx
import re
import os

# Set path to cwd; make in/ and out/ dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))
if not os.path.exists('in'): os.mkdir('in')
if not os.path.exists('out'): os.mkdir('out')

def read_input_file(path):
    """
    Parses an input file

    :param path: str, a path
    :return: networkx Graph is the input is well formed, None otherwise
    """
    with open(path, 'r') as fo:
        n = fo.readline().strip()
        assert n.isdigit()
        n = int(n)

        lines = fo.read().splitlines()
        fo.close()

        # validate lines
        for line in lines:
            tokens = line.split(' ')

            assert len(tokens) == 3
            assert tokens[0].isdigit()
            assert tokens[1].isdigit()
            assert int(tokens[0]) < n
            assert int(tokens[1]) < n
            assert bool(re.match(r'(^\d+\.\d{1,3}$|^\d+$)', tokens[2]))

        G = nx.parse_edgelist(lines, nodetype=int, data=(('weight', float),))
        G.add_nodes_from(range(n))

        assert nx.is_connected(G)

        return G



def write_input_file(G, path):
    with open(path, 'w') as fo:
        n = len(G)
        lines = nx.generate_edgelist(G, data=['weight'])
        fo.write(str(n) + '\n')
        fo.writelines('\n'.join(lines))
        fo.close()

def read_output_file(path):
    with open(path, 'r') as fo: 
        nodes = fo.readline()
        lines = fo.read().splitlines()
        fo.close()
        T = nx.parse_edgelist(lines, nodetype=int, data=(('weight', float),))
        T.add_nodes_from(map(int, nodes.split()))
        return T

def write_output_file(T, path):
    with open(path, 'w') as fo: 
        fo.write(' '.join(map(str, T.nodes)) + '\n')
        lines = nx.generate_edgelist(T, data=['weight'])
        fo.writelines('\n'.join(lines))
        fo.close()
