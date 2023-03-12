import pandas as pd
import csv
import itertools
df = pd.read_json('response.json')
df.to_csv('APPLEhistorydata.csv', index=False)


with open('APPLEhistorydata.csv', 'r') as file:
    reader = csv.reader(file)

    
    rows = [list(row) for row in itertools.zip_longest(*reader, fillvalue='')]
    
    # Obliczenie maksymalnej szerokości kolumny na podstawie danych w każdej kolumnie
    col_widths = [max(len(str(cell)) for cell in column) for column in rows]

    # Wydrukowanie danych w ładnym formacie z uwzględnieniem maksymalnej szerokości kolumn
    for row in rows:
        print('  '.join(str(cell).ljust(width) for cell, width in zip(row, col_widths)))
