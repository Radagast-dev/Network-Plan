import sys
import csv

class NetNode:
    def __init__(self, number, successor, name, content, FAZ, SAZ, FEZ, SEZ, GP, FP):
        self = self
        self.number = number
        self.successor = successor
        self.name = name
        self.content = content
        #self.time = time #anpassen dummy time variable
        self.FAZ = FAZ
        self.SAZ = SAZ
        self.FEZ = FEZ
        self.SEZ = SEZ
        self.GP = GP
        self.FP = FP
    
    def __del__(self): #destructor --> needed?
        print("Node ", self, " deleted!")

    def buildNodesFromCSV(self):        #idee: nodes vorab ohne werte aber mit ptr bauen
        print("Init all nodes needed + show nodes are existing")

    def fillNodesWithValues(self):      #idee: hier werden die werte aus der csv genommen und gelesen
        print("Inhalt FAZ SEZ usw rein in die Nodes!")