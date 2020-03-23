from flask import Flask, render_template, jsonify
# Importa el modulo sqlite3
import sqlite3
import json

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')
    
@app.route('/lastStop')
def lastStop():
    
    return render_template('lastStop.html')

@app.route('/consulta')
def consulta():
    
    # Crea una conexion a la base de datos SQLite
    con = sqlite3.connect('stops.db3')

    # Con la conexion, crea un objeto cursor
    cur = con.cursor()

    # Ejecuta la consulta
    cur.execute('SELECT * FROM registros ORDER by Id DESC LIMIT 30')
    # Extrae todos los datos
    result = cur.fetchall()
    #print(result)

    lista = [{"Id": x[0], "beaconMAC": x[1], "dateTimeDetection": x[2], "hourDetection": x[3], "dayDetection": x[4], "monthDetection": x[5], "yearDetection": x[6]} for x in result]
    #print(lista)
    return jsonify(lista)

@app.route('/consultaLastStop')
def consultaLastStop():
    
    # Crea una conexion a la base de datos SQLite

    con = sqlite3.connect('stops.db3')

    # Con la conexion, crea un objeto cursor
    cur = con.cursor()


    cur.execute('SELECT * FROM registros ORDER by Id DESC LIMIT 1')
    # Extrae todos los datos
    result = cur.fetchall()
    #print(result)

    listaLastStop = [{"Id": x[0], "beaconMAC": x[1], "dateTimeDetection": x[2], "hourDetection": x[3], "dayDetection": x[4], "monthDetection": x[5], "yearDetection": x[6]} for x in result]
    
    return jsonify(listaLastStop)

if __name__ == '__main__':
    app.run(debug=True)
