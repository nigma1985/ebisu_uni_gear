import glob, os
# from db import database
# from module import json2py
# from module.connectPostgreSQL import database
# from module.import_moves import mact2sql
# from openpyxl import Workbook
import csv
import networkx as nx
from operator import itemgetter
# import community #This is the python-louvain package we installed.
from multiprocessing import Pool
import itertools

os.chdir("../ebisu_uni_gear/")


with open('input/input_network.csv', newline = '') as csvfile:
# with open('quakers_nodelist.csv', 'r') as csvfile:
    nodereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    # for row in nodereader:
    #     print(', '.join(row), type(row))
    nodes = [n for n in nodereader][1:]

node_names = [n[0] for n in nodes] # Get a list of only the node names

with open('input/input_network.csv', 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data

print(len(node_names))
print(len(edges))

# G = nx.Graph()
#
# G.add_nodes_from(node_names)
# G.add_edges_from(edges)

#
# wb = Workbook()
#
# ws['A1']
