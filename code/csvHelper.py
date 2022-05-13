import sys
import os
import csv

filePath = "csv\input_n.csv"
    #Dictionary zum einlesen
csvDict = {}   #key:value!

class CsvHelper():

    #Eigenschaften
    file = "input_n.csv"

    #Liste für eingelesene CSV werte
    thisList = []   #Kommaseparation

    #Init + Funktionen
    def __init__(self, csvDict, thisList):
        csvDict = csvDict
        thisList = thisList
        print("Hello helper here!")
    
    def readCsv():  ##lese ein und printe funzt soweit
        print("Reading the csv!")
        with open(filePath, 'r') as csv_File:
            reader = csv.reader(csv_File, delimiter=',')
            for row in reader:
                print(row)

            #schreibe in dictionary

            #header abschnippeln
            #klammern am anfang+ ende entfernen

    def csvValuesToNodes(): #add csv vals to nodes + instantiate nodes (1 per key:value pair)
        print("Adding csv vals to nodes")