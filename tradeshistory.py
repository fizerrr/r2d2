import json
import csv

def tradeshistory(data):
# zapisanie danych do pliku JSON
    with open("tradeshistory.json", "w") as json_file:
        json.dump(data, json_file,indent=4)
def getallsymbols(data1):
    with open("getallsymbols.json", "w") as json_file:
        json.dump(data1, json_file,indent=4)

    