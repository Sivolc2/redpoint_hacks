import json
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import operator

def read_character_locations(filename):
    locs = []
    lastChar = None
    with open(filename, 'r') as file:
        file.readline()
        for idx, line in enumerate(file):
            cols = line.rstrip().split("\t")
            charid = int(cols[14])
            if charid != -1 and charid != lastChar:
                locs.append((charid, idx))
            lastChar = charid
    return locs

def get_character_names(filename):
    names = {}
    with open(filename, 'r') as file:
        data = json.load(file)
        for character in data["characters"]:
            idd = int(character["id"])
            char_names = character["names"]
            names[idd] = char_names[0]["n"]
    return names

def get_character_coocurrence_counts(character_names, locs, window=25):
    nodes = Counter()
    edges = {}

    for idx, (char_id, loc) in enumerate(locs):
        name1 = character_names[char_id]
        nodes[name1] += 1
        if name1 not in edges:
            edges[name1] = Counter()

        nextChar = idx
        while nextChar < len(locs) - 1:
            nextChar += 1
            (next_char_id, next_loc) = locs[nextChar]
            if next_loc - loc > window:
                break
            name2 = character_names[next_char_id]
            if next_char_id != char_id:
                edges[name1][name2] += 1

    return nodes, edges


def create_graph(nodes, edges, min_edge_weight=5):
    G = nx.Graph()
    for person, node_size in nodes.items():
        G.add_node(person, nodesize=node_size)
        
    for person1, connections in edges.items():
        for person2, weight in connections.items():
            if weight > min_edge_weight:
                G.add_weighted_edges_from([(person1, person2, weight)])
    return G

def display_graph(G):
    """ Plot a set of weighted nodes and weighted edges on a network graph """
    force_directed_expansion = 10
    figure_height = 20
    figure_width = 20

    options = {
        'edgecolors': "black",
        'linewidths': 1,
        'with_labels': True,
        'font_weight': 'regular'
    }
    
    sizes = [G.nodes[node]['nodesize'] for node in G]
    weights = [G[u][v]['weight']/100. for u, v in G.edges()]

    fig, ax = plt.subplots(figsize=(figure_height, figure_width))
    nx.draw_networkx(G, pos=nx.spring_layout(G, k=force_directed_expansion, iterations=100), node_size=sizes, width=weights, **options)
    plt.show()

def print_top(measure, n=5):
    sorted_measure = sorted(measure.items(), key=operator.itemgetter(1), reverse=True)
    for node, val in sorted_measure[:n]:
        print(f"{node}\t{val:.3f}")

if __name__ == "__main__":
    character_locs = read_character_locations("./data/pride_and_prejudice.tokens")
    character_names = get_character_names("./data/pride_and_prejudice.tokens")
    nodes, edges = get_character_coocurrence_counts(character_names, character_locs, window=25)
    G = create_graph(nodes, edges)
    display_graph(G)
    
    # Analyzing and printing top nodes based on different centrality measures
    print("Top nodes based on degree centrality:")
    degree_centrality = nx.degree_centrality(G)
    print_top(degree_centrality)

    print("\nTop nodes based on betweenness centrality:")
    betweenness_centrality = nx.betweenness_centrality(G)
    print_top(betweenness_centrality)

    print("\nTop nodes based on closeness centrality:")
    closeness_centrality = nx.closeness_centrality(G)
    print_top(closeness_centrality)
