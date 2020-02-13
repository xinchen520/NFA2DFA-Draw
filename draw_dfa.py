import sys
import csv
import matplotlib.pyplot as plt
import networkx as nx
import pydot
argv = sys.argv

if len(argv) != 2:
    print("usage: python "+argv[0] + " file.csv")
    
    sys.exit(1)

with open(argv[1]) as csv_file:
    input_symbols = []
    found_table = False
    edges = {}
    accepts = {}
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if found_table and row[0][:5] != 'start':
            u = row[0].strip()
            i=0
            for v in row[1:len(input_symbols)+1]:
                v = v.strip()
                e = (u,v)
                if edges.get(e):
                    edges[e] = edges[e] + "|" + input_symbols[i]
                else:
                    edges[e] = input_symbols[i]
                i+=1
            if row[-1].strip() == 'true':
                accepts[row[0].strip()] = True
            else:
                accepts[row[0].strip()] = False
        if row[0][:11] == 'state\\input':
            found_table = True
            for x in row[1:]:
                if x.endswith('accept'):
                    break
                else:
                    input_symbols.append(x.strip())
    G = nx.MultiDiGraph()
    G.add_nodes_from(accepts.keys())
    G.add_edges_from(edges.keys())
    pos = nx.spring_layout(G)
    P = nx.drawing.nx_pydot.to_pydot(G)
    for edge in P.get_edges():
        e = (edge.get_source(),edge.get_destination())
        label = edges[e]
        edge.obj_dict['attributes']['label'] =  label
    for node in P.get_node_list():
        name = node.get_name()
        if name == '1':
                node.set('shape', 'octagon')
        if accepts[name]:
            node.set('shape','doublecircle')
            if name == '1':
                node.set('shape', 'doubleoctagon')
    outpath = argv[1] + ".png"
    P.write_png(outpath)
    print("Output image written to " + outpath)