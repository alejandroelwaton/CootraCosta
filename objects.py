import numpy as np
import os
from time import sleep


def clear():
    text = ''
    sistema = os.sys.platform
    if sistema == 'win32':
        text = 'cls'
    elif sistema == "Linux" or sistema == "Darwin":
        text = "clear"
    else:
        print('Tu sistema operativo no es compatible')
    os.system(text)



class Rutas :
    def __init__(self, origen:str,destino:str, horario:int, costo:int):
        self.origen = origen
        self.destino = destino 
        self.horario = horario
        self.costo = costo

        

class Buses:
    def __init__(self, numero:int, placa:str, conductor:str, mal_estado:list, filas:int = 4, columnas:int = 10):
        self.numero = numero
        self.placa = placa
        self.mal_estado = mal_estado 
        self.conductor = conductor
        self.filas = filas
        self.columnas = columnas
    
    
    def crear_asientos(self):
        filas = self.filas
        columnas = self.columnas
        #asientos libres por defecto
        self.asientos = np.zeros((filas,columnas))
        return self.asientos


    def asignar_mal_estado(self):
        mal_estado = self.mal_estado
        for i in mal_estado:
            self.asientos[i[0],i[1]] = 2


    def asignar_asiento(self, fila, columna):
        if self.asientos.all() == 0:
            self.asientos[fila, columna] = 1


    def mostrar_asientos(self):
        print(self.asientos)
        print(f'El conductor del bus {self.conductor} atiende en el bus {self.numero} con placa {self.placa}')
        sleep(2)


#hasta aqui vamos bien
class Pasajero:
    def __init__(self, nombre:str, ID:int, edad:int, ruta:object, hora_comprado:int, puestos:int, efectivo:int):
        self.nombre = nombre
        self.apellido = ID
        self.edad = edad
        self.ruta = ruta
        self.hora_comprado = hora_comprado
        self.puestos = puestos
        self.efectivo = efectivo


    def mostrar_ruta(self):
        print(f'{self.ruta.origen} - {self.ruta.destino}')
        sleep(2)

    
    def etapas(self):
        if self.edad in range(0, 14):
            return 'Infantil'
        elif self.edad in range(14, 18):
            return 'Adolescente'
        elif self.edad in range(18, 60):
            return 'Adulto'
        else:
            return 'No aplica'

    
    def comprobar_puestos(self):
        if self.puestos >= 3:
            return True
        else:
            pass
            

    def comprobar_efectivo(self):
        if self.efectivo >= self.ruta.costo:
            self.efectivo -= self.ruta.costo
            return True
        else:
            print('No tiene dinero suficiente')
    

    def comprobar_hora(self):
        if self.hora_comprado <= self.ruta.horario:
            return True
        else:
            print('No se puede comprar en horario anterior')


    def comprobar_edad(self):
        if self.edad >= 18:
            return True
        else:
            print('Un menor no puede comprar un asiento')


    def comprar_asiento(self, fila, columna, bus:object):
        vuelto = f', su vuelto es  de {self.efectivo}'
        if self.comprobar_efectivo() == True and self.comprobar_hora() == True and self.comprobar_edad() == True:
            bus.asignar_asiento(fila, columna)
            self.puestos += 1
            print(f'Asiento comprado por {self.nombre} a las {self.hora_comprado}, por un total de {self.ruta.costo} pesos {vuelto if self.efectivo > 0 else ""}')
            sleep(2)
            if self.puestos == 3:
                self.ruta.costo /=2
        else:
            #mostrar la razon por la cual el pasajero no puede comprar el asiento
            print(f'No se puede comprar el asiento porque {self.nombre} no cumple con los requisitos')



