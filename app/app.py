from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)


def variants(chrom, pos, aft):
#connect met de database
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'gnomad'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
#query die zoekt naar varianten die de chromosoom, positie en alternative van de user input bevatten.
    query = 'SELECT * FROM variants WHERE chrom=%s AND pos=%s AND aft=%s;'
    cursor.execute(query, (chrom,pos,aft))
    results = cursor.fetchone()
    cursor.close()
    connection.close()
    return results

#api die de user input meegeeft
@app.route('/')
def index():
    chrom = request.args.get('chrom')
    pos =  request.args.get('pos')
    aft =  request.args.get('aft')
    results = variants(chrom, pos, aft)
    return str(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
