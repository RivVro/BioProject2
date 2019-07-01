def vulDatabase():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'gnomad'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = 'SELECT * FROM variants'
    #query = 'BULK INSTERT variants FROM databaseData WITH (FIELDTERMINATOR =',')'
    cursor.execute(query)
    cursor.close()
    connection.close()
    for row in cursor:
        print (row)
    #return ("database gevuld!")

def main():
    vulDatabase()
