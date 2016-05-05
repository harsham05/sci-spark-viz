import xmltodict, json, functools
import networkx as nx
from pprint import pprint
import graphviz as gv

def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


def main():
    
    inF = open('graphEdges', 'r')        
    tuples = eval(inF.readline())
    inF.close()

    G = nx.DiGraph(tuples)
    weakGraphs = []
    for w in nx.weakly_connected_component_subgraphs(G):
        weakGraphs.append(w.edges())


    weakGraphs.sort(key=lambda x: len(x), reverse=True)

    subGraph = weakGraphs[1]


    digraph = functools.partial(gv.Digraph, graph_attr={"rankdir": "LR"}, format='svg') #"ordering":"out"
    nodes = set()
    for edgeTup in subGraph:
        nodes.add(edgeTup[0])
        nodes.add(edgeTup[1])
    nodes = list(nodes)
    edges = subGraph

    add_edges(add_nodes(digraph(), nodes), edges).render('img/g4')


    """
    with open('img/g4.svg') as fd:
        doc = xmltodict.parse(fd.read())

        #print doc["svg"]["g"]["g"].keys()

        with open('img/data.json', 'w') as outfile:
            json.dump(doc, outfile)
    """







    '''
    #nx.shortest_path(G, 'A', 'D', weight='weight')

    for tup in tuples:
        try:            
            graphEdgeDict[tup[0]].append(tup[1])
        except KeyError:
            graphEdgeDict[tup[0]] = [tup[1]]


    print sorted(graphEdgeDict, key=graphEdgeDict.get)

    # sort it
    for key in sorted(graphEdgeDict.iterkeys()):
        print "%s: %s" % (key, mydict[key])


    square = functools.partial(power, exponent=2)
    cube = functools.partial(power, exponent=3)

    def test_partials():
        assert square(2) == 4
        assert cube(2) == 8

    '''
    
    
if __name__ == "__main__":
    main()

def getD3jsonObj():

    jsonObj = {"nodes": [], "edges": []}
    nodes = set()
    for edgeTup in givenGraph:
        nodes.add(edgeTup[0])
        nodes.add(edgeTup[1])

    hashMap = {}
    value = 0
    for elem in nodes:
        hashMap[elem] = value
        value += 1

        name = {"name": elem}
        jsonObj["nodes"].append(name)

    for edgeTup in givenGraph:
        edgeDict = {"source": hashMap[edgeTup[0]], "target": hashMap[edgeTup[1]]}
        jsonObj["edges"].append(edgeDict)

    pprint(jsonObj)