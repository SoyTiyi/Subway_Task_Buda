import sys
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

class Subway:

    """ This function create and use metworkx using dijkstra to find the shortest path """
    def shortestPath(self,row,column,nodes,source,target):

        """ Graph """
        G = nx.Graph()

        """ Add nodes """
        for node in nodes:
            G.add_node(node)

        """ Add edges """
        for i in range(0,len(row)):
            G.add_weighted_edges_from([(row[i],column[i],1)])

        """ Get Shortest path using dijkstra algorithm """
        path = nx.dijkstra_path(G,source=source,target=target)

        print(path)
        return path
        



    """ Function that handle all the input data that we need to solve the problem """
    def handleInput(self, fileName,initialStation,finalStation,subwayColor):
        row=[]
        column=[]
        nodes=[]
        
        with open(fileName,"r") as f:
            
            lines = f.readlines()

            """ Read all the lines of the txt file """
            for line in lines:
            
                """ Clean and handle input """
                node, characteristic = line.strip()[:-1].replace('"','').split(": ")
                nodeColor = characteristic[:-1].split(",")[-1]
                nodesAdjacent = characteristic[1:-1].split(",")[:-1]
                nodes.append(node)

                """ Choose nodes that are enable for the color of the subway """

                if(nodeColor == subwayColor or nodeColor=="none"):
                    for adjacent in nodesAdjacent:
                        row.append(node)
                        column.append(adjacent)

            """ Join the nodes with enables nodes after deleted "corrupt" nodes """

            for i in range(len(column)):
                if column[i] not in row:
                    for j in range(len(column)):
                        if(column[i] == column[j] and row[i]!=row[j]):
                            column[i] = row[j]
                            column[j] = row[i]

            """ This method return the solution """
            return self.shortestPath(row,column,nodes,initialStation,finalStation)


