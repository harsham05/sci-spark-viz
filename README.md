
1. graphViz for OS X (http://www.graphviz.org/pub/graphviz/stable/macos/mountainlion/graphviz-2.36.0.pkg)

2. GraphViz python wrapper library (pip install graphviz)

3. networkX library (should be available if you have installed Anaconda)

4. pip install xmltodict


``` 
python genSubGraph.py /path/to/static/js/girl_names_us.js no_of_subgraphs_to_generate /path/to/edgeList


Eg: 

python genSubGraph.py girl_names_us.js 4 graphEdges.txt

```