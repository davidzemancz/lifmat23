import sqlite3
import csv

class TableColumn:
    def __init__(self, name, data_type) -> None:
        self.name = name
        self.data_type = data_type

    def __repr__(self) -> str:
        return f'{self.name} {self.data_type}'

# Read data from CSV
tables = {}
with open("..\data\DLP_datove_rozhrani20230601.csv") as data_spec_csv:
    reader = csv.reader(data_spec_csv, delimiter=';')
    next(reader)
    for row in reader:
        table = row[0]
        index = int(row[1])
        col = row[2]
        data_type = row[3]
        if (data_type.startswith('DATE')):
            data_type = 'DATE'
        desc = row[4]
        if not tables.get(table):
            tables[table] = []
        tables[table].append(TableColumn(col, data_type))

# Create tables and insert data into them
con = sqlite3.connect("data.db") 
for table_name in tables:
    cur = con.cursor()

    print(table_name)

    cur.execute(f'DROP TABLE IF EXISTS {table_name}')
    query = f'CREATE TABLE {table_name} ({", ".join([col.name + " " + col.data_type for col in tables[table_name]])});'
    cur.execute(query)

    with open(f'..\data\dlp\{table_name}.csv','r') as data_csv:
        reader = csv.reader(data_csv, delimiter=';')
        to_db = [tuple(row) for row in reader]
    cur.executemany(f'INSERT INTO {table_name} ({", ".join([col.name for col in tables[table_name]])}) VALUES ({",".join(["?" for col in tables[table_name]])});', to_db)
    con.commit()


# Global table
cur = con.cursor()
table_name = 'leky'
cur.execute(f'DROP TABLE IF EXISTS {table_name}')
query = f'CREATE TABLE {table_name} (KOD_SUKL, NAZEV, SPC);'
cur.execute(query)


exit()