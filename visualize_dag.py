import os
import re
from collections import defaultdict
import graphviz
G = graphviz.Digraph()
pwd = os.getcwd()
dir = pwd + "/tmp/"
print dir
visited = {}
edges = defaultdict(list)
for filename in os.listdir(dir):
    os.chdir(dir)
    with open(filename, 'rU') as f:
         t = f.read()
         matches=re.findall(r'\`(.+?)\`',t)
         visited[filename] = False
         for match in matches:
             str = "tmp_" + filename
             if str.endswith(".sql"):
                 str = str[:-4]
             edges[match].append(str)
             G.edge(match,str)
             visited[match] = False
             visited[str] = False

dir = pwd + "/final/"
print dir
for filename in os.listdir(dir):
    os.chdir(dir)
    with open(filename, 'rU') as f:
         t = f.read()
         matches=re.findall(r'\`(.+?)\`',t)
         visited[filename] = False
         for match in matches:
             str = "final_" + filename
             if str.endswith(".sql"):
                 str = str[:-4]
             edges[match].append(str)
             G.edge(match,str)
             visited[match] = False
             visited[str] = False
os.chdir(pwd)
if not os.path.exists(pwd+"/Output/"):
    os.makedirs("Output")
os.chdir(pwd+"/Output/")
if os.path.exists('./Output.gv'):
    os.remove("Output.gv")

if os.path.exists('./Output.gv.pdf'):
    os.remove("Output.gv.pdf")
G.render('Output.gv', view=False)

for u, v in edges.items():
    str = u + "->( "
    for x in v:
        str+= x + " "
    print str + ") "

def topologicalSortUtil(v,visited,stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in edges[v]:
            if visited[i] == False:
                topologicalSortUtil(i,visited,stack)

        # Push current vertex to stack which stores result
        stack.insert(0,v)

def topologicalSort():
        # Mark all the vertices as not visited
        stack =[]
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for u, v in edges.items():
            if visited[u] == False:
                topologicalSortUtil(u,visited,stack)

        # Print contents of the stack
        print stack
        os.chdir(pwd);
        return stack

stack=topologicalSort();
