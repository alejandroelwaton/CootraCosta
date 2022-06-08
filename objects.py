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
        self.costo_descuento = costo /2

        

class Buses:
    def __init__(self, numero:int, placa:str, conductor:str, mal_estado:list, filas:int = 4, columnas:int =10 , ruta:object = None):
        self.numero = numero
        self.placa = placa
        self.mal_estado = mal_estado 
        self.conductor = conductor
        self.filas = filas
        self.columnas = columnas
        self.ruta = ruta

    
    def modificar_bus(self, rutas:list):
        self.numero = int(input('numero del bus: '))
        self.placa = input('placa del bus: ')
        self.conductor = input('conductor del bus: ')
        i = int(input('Ingrese un numero: '))
        while i > 0:
            i -= 1
            filas = int(input('Fila del asiento en mal estado: '))
            columnas = int(input('Columna del asiento en mal estado: '))
            asiento_mal_estado = [[filas, columnas]]
            self.mal_estado.append(asiento_mal_estado)
        self.filas = int(input('filas del bus: '))
        self.columnas = int(input('Columnas del bus: '))

        for ruta in rutas:
            print(f'{rutas.index(ruta)+1}, {ruta.origen} -> {ruta.destino}')
        ruta_bus = input('Ruta que seguira el bus: ')
        for ruta in rutas:
            if ruta_bus == rutas.index(ruta)-1:
                ruta_bus = ruta

    

    def anadir_bus(rutas:list):
        numero = int(input('numero del bus: '))
        placa = input('placa del bus: ')
        conductor = input('conductor del bus: ')
        puestos_mal_estado = int(input('Cantidad de puestos en mal estado: '))
        while puestos_mal_estado > 0:
            asientos_mal_estado = []
            filas = int(input('Fila del asiento en mal estado: '))
            columnas = int(input('Columna del asiento en mal estado: '))
            asientos_mal_estado.append([filas, columnas])
            puestos_mal_estado -= 1
        mal_estado = [asientos for asientos in asientos_mal_estado]
        print(mal_estado)
        for ruta in rutas:
            print(f'{rutas.index(ruta)+1}, {ruta.origen} -> {ruta.destino}')
        ruta_bus = input('Ruta que seguira el bus: ')
        for ruta in rutas:
            if ruta_bus == rutas.index(ruta)-1:
                ruta_bus = ruta

        nuevo_bus = Buses(numero, placa, conductor, mal_estado, filas, columnas, ruta)
        return  nuevo_bus

    
    def crear_asientos(self):
        filas = self.filas
        columnas = self.columnas
        #asientos libres por defecto
        self.asientos = np.zeros((filas,columnas))
        return self.asientos


    def asignar_mal_estado(self):
        mal_estado = self.mal_estado
        for fila, columna in mal_estado:
            self.asientos[fila,columna] = 2


    def comprobar_asientos_libres(self, fila:int, columna:int):
        self.asignar_mal_estado()
        if self.asientos[fila][columna] == 0:
            return True
        else:
            return False


    def mostrar_asientos(self):
        print(self.asientos)
        print(f'El conductor del bus {self.conductor} atiende en el bus {self.numero} con placa {self.placa}')
        sleep(2)


#hasta aqui vamos bien
class Pasajero:
    def __init__(self, nombre:str, ID:int, edad:int, hora_comprado:int, puestos:int, efectivo:int):
        self.nombre = nombre
        self.apellido = ID
        self.edad = edad
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
            

    def comprobar_efectivo(self, ruta:object):
        if self.efectivo >= (ruta.costo_descuento if self.puestos > 3 else ruta.costo):
            return True
        else:
            return False
    

    def comprobar_hora(self, ruta:object):
        if self.hora_comprado <= ruta.horario:
            return True
        else:
            return False


    def comprobar_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False


    def comprar_asiento(self, fila, columna, bus:object, ruta:object):
        self.ruta = ruta
        print(f'{self.nombre} su dinero:  {self.efectivo}')
        if self.comprobar_hora(ruta) == True and self.comprobar_edad():
            if bus.comprobar_asientos_libres(fila, columna) == True and self.comprobar_efectivo(ruta) == True and bus.ruta == ruta:
                self.efectivo -= (ruta.costo_descuento if self.puestos >= 3 else ruta.costo)
                bus.asientos[fila, columna] = 1
                self.puestos += 1
                vuelto = f'Su vuelto es  de {self.efectivo}'
                print(
                f'''Ticket a nombre de {self.nombre}:
                Ruta: {self.ruta.origen} -> {self.ruta.destino}
                Hora: {self.ruta.horario}
                Costo: {ruta.costo_descuento if self.puestos > 3 else ruta.costo}
                Puestos: {self.puestos}
                Efectivo: {self.efectivo}
                {'' if self.efectivo <= ruta.costo or self.efectivo <= ruta.costo_descuento else vuelto} ''')
                sleep(2)
            else:
                print(''if bus.comprobar_asientos_libres(fila, columna) == True else 'No hay asientos libres')
                print(''if self.comprobar_efectivo(ruta) == True else 'No tiene suficiente dinero')
                print('' if bus.ruta == ruta else "No se puede comprar en este bus")
        else:
            print('' if self.comprobar_hora(ruta) == True else "No se puede comprar en horario anterior")
            print('' if self.comprobar_edad() == True else "Un menor no puede comprar un asiento")

        