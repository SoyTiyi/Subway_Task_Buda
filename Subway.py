import sys
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


""" This function create and use metworkx using dijkstra to find the shortest way """
def solution(row,column,nodes,source,target):
    G = nx.Graph()

    for node in nodes:
        G.add_node(node)

    for i in range(0,len(row)):
        G.add_weighted_edges_from([(row[i],column[i],1)])
    
    path = nx.dijkstra_path(G,source=source,target=target)
    print("The shortest way is", path)
    



""" Function that handle all the input data that we need to solve the problem """
def handleInput():
    row=[]
    column=[]
    nodes=[]

    print("What is the Initial Station?")
    initialStation = sys.stdin.readline().strip()
    print("What is the Final Station?")
    finalStation = sys.stdin.readline().strip()
    print("What is the color of the subway(red or green)?")
    subwayColor = sys.stdin.readline().strip()
    
    with open("input.txt","r") as f:
        
        lines = f.readlines()
        for line in lines:
            node, characteristic = line.strip()[:-1].replace('"','').split(": ")
            nodeColor = characteristic[:-1].split(",")[-1]
            nodesAdjacent = characteristic[1:-1].split(",")[:-1]
            nodes.append(node)
            if(nodeColor == subwayColor or nodeColor=="none"):
                for adjacent in nodesAdjacent:
                    row.append(node)
                    column.append(adjacent)

        for i in range(len(column)):
            if column[i] not in row:
                for j in range(len(column)):
                    if(column[i] == column[j] and row[i]!=row[j]):
                        column[i] = row[j]
                        column[j] = row[i]
        
        print(row)
        print(column)
        print(nodes)
        print(initialStation)
        print(finalStation)
        solution(row,column,nodes,initialStation,finalStation)
        

       


def main():
    handleInput()
    


if __name__ == "__main__":
    main()