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


    # iterate through all weakGraphs here, lay them out one on top of another
    yPos = -3
    for i in range(0, 3):
        yPos += 3

        digraph = functools.partial(gv.Digraph, graph_attr={"rankdir": "LR"}, format='svg') #"ordering":"out"
        nodes = set()
        for edgeTup in weakGraphs[i]:
            nodes.add(edgeTup[0])
            nodes.add(edgeTup[1])
        nodes = list(nodes)
        edges = weakGraphs[i]

        add_edges(add_nodes(digraph(), nodes), edges).render('img/g4')

        with open('img/g4.svg') as fd:
            doc = xmltodict.parse(fd.read())

            nodeYLocation = {}
            for elem in doc["svg"]["g"]["g"]:
                if elem["@class"] == "node":
                    #(Cx, Cy) x, y coordinates of center, origin top left corner
                    #(Rx, Ry) radius of ellipse along x, y axes
                    nodeYLocation[elem["title"]] = int(elem["ellipse"]["@cy"])

            #minNode = max(nodeYLocation, key=nodeYLocation.get)
            #maxNode = min(nodeYLocation, key=nodeYLocation.get)
            #diff = nodeYLocation[minNode] - nodeYLocation[maxNode]
            #print diff/9.0


            #for every 24 change in y coordinate, place a node, in json
            for key in nodeYLocation:
                nodeYLocation[key] /= -9
                nodeYLocation[key] += yPos


            with open("blah.json") as jsonF:
                jsonData = eval(jsonF.read())
                for lineDict in jsonData:
                    for node in lineDict["values"]:
                        try:
                            node["position"] = nodeYLocation[node["name"]]
                        except KeyError:
                            continue

                with open("img/girl_names_us.js", "w") as outF:
                    json.dump(jsonData, outF, indent=4, sort_keys=True, separators=(',', ': '))


                data = None
                with open("img/girl_names_us.js", "r") as original:
                    data = original.read().lstrip("[")

                with open("img/girl_names_us.js", "w") as modified:
                    modified.write("var girls = [\n" + data)




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