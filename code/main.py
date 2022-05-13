import sys
import csv
from netNode import NetNode
from csvHelper import CsvHelper

#Variablen
FAZ_temp = 0

#STUFF

#einlesen csv
#https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
#https://ingo-janssen.de/csv-dateien-lesen-mit-python/

#aufbau der instanzen
#http://python4kids.net/how2think/kap17.htm

#berechnung

#ausgabe csv

#ausgabe grafik

#STUFF

#Testinit Klassen
net = NetNode
net.buildNodesFromCSV(net)
net.fillNodesWithValues(net)

helper = CsvHelper
helper.readCsv()