import sqlite3
import csv

class TableColumn:
    def __init__(self, name, data_type) -> None:
        self.name = name
        self.data_type = data_type

    def __repr__(self) -> str:
        return f'{self.name} {self.data_type}'

def create_db():

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

        with open(f'..\data\dlp\{table_name}.csv','r', encoding='windows-1250') as data_csv:
            reader = csv.reader(data_csv, delimiter=';')
            to_db = [tuple(row) for row in reader]
        cur.executemany(f'INSERT INTO {table_name} ({", ".join([col.name for col in tables[table_name]])}) VALUES ({",".join(["?" for col in tables[table_name]])});', to_db)
        con.commit()

def create_leky():
    con = sqlite3.connect("data.db") 
    # Global table
    cur = con.cursor()

    view_name = 'leky_view'
    cur.execute(f'DROP VIEW IF EXISTS {view_name}')
    query = f'CREATE VIEW {view_name} AS SELECT lp.KOD_SUKL, (lp.NAZEV || " " || lp.SILA) AS NAZEV, nd.SPC FROM dlp_lecivepripravky lp, dlp_nazvydokumentu nd WHERE lp.KOD_SUKL = nd.KOD_SUKL;'
    cur.execute(query)
    con.commit()

    table_name = 'leky'
    print(table_name)
    cur.execute(f'DROP TABLE IF EXISTS {table_name}')
    query = f'CREATE TABLE {table_name} AS SELECT * FROM {view_name}'
    cur.execute(query)
    con.commit()

    query = f'ALTER TABLE {table_name} ADD NEMOC VARCHAR;'
    cur.execute(query)
    con.commit()

    for lek in ['PARALEN','IBUPROFEN','ASPIRIN']:
        nemoc = 'horecka'
        query = f'UPDATE {table_name} SET NEMOC = "{nemoc}" WHERE UPPER(NAZEV) LIKE "%{lek}%"'
        cur.execute(query)
        con.commit()

    # query = f'SELECT NAZEV, COUNT(NAZEV) AS CNT FROM dlp_lecivepripravky GROUP BY NAZEV ORDER BY CNT DESC LIMIT 20'
    # cur.execute(query)
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)
# create_db()
create_leky()

exit()
