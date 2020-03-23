#!/usr/bin/python

import time
import sqlite3

#from gattlib import BeaconService
from gattlib import DiscoveryService

service = DiscoveryService()
devices = service.discover(3) #3 segundos 

while True:
    for address, name in devices.items():
    #print("nombre: {}, direccion: {}".format(name, address))
        
        varDateTime = time.strftime("%c")
        varHour = time.strftime("%H:%M:%S")
        varDay = time.strftime("%d")
        varMonth = time.strftime("%B")
        varYear = time.strftime("%Y")
        varBeaconMAC = address
        #print(devices.items())
        #varBeaconMAC = address, name in devices.items()
        print("Fecha y hora de la deteccion: "+ varDateTime)
        print("Hora de la deteccion: "+ varHour)
        print("Dia de la deteccion: "+ varDay)
        print("Mes de la deteccion: "+ varMonth)
        print("Anio de la deteccion: "+varYear)
        print("Direccion MAC del Beacon detectado: "+ varBeaconMAC)
        #os.system("python connectDB.py")
        
        con = sqlite3.connect('stops.db3')

        def sql_insert(con, entities):

            cursorObj = con.cursor()

            cursorObj.execute('INSERT INTO registros(BeaconMAC, dateTimeDetection, hourDetection, dayDetection, monthDetection, yearDetection) VALUES(?, ?, ?, ?, ?, ?)', entities)

            con.commit()
            
        entities = (varBeaconMAC, varDateTime, varHour, varDay, varMonth, varYear)
            
        sql_insert(con, entities)
            
        con.close()
        
    time.sleep(5)
