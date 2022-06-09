import numpy as np
import os


def verificarSiEsEntero(númeroDigitado: str):
    # Retorna True o False si es posible la conversión
    try:
        int(númeroDigitado)
        elNúmeroEsEntero = True
    except:
        elNúmeroEsEntero = False
    return elNúmeroEsEntero


class Rutas :
    def __init__(self, origen:str,destino:str, horario:int, costo:int):
        self.origen = origen
        self.destino = destino 
        self.horario = horario
        self.costo = costo
        self.costo_descuento = costo /2

    def anadir_ruta(self):
        while True:
            origen = input('Origen: ')
            destino = input('Destino: ')
            horario = int(input('Horario: '))
            while verificarSiEsEntero(horario) == False and horario > 23:
                horario = int(input('Horario: '))
            costo = int(input('Costo: '))
            while verificarSiEsEntero(costo) == False:
                costo = int(input('Costo: '))

            nueva_ruta = Rutas(origen, destino, horario, costo)
            return nueva_ruta

        

class Buses:
    def __init__(self, numero:int, placa:str, conductor:str, mal_estado:list, ruta:object = None):
        self.numero = numero
        self.placa = placa
        self.mal_estado = mal_estado 
        self.conductor = conductor
        self.ruta = ruta
        self.asientos_vendidos = 0

    
    def modificar_bus(self, rutas:list):
        self.numero = int(input('numero del bus: '))
        while verificarSiEsEntero(self.numero) == False:
            self.numero = int(input('numero del bus: '))
        self.placa = input('placa del bus: ')
        self.conductor = input('conductor del bus: ')
        i = int(input('Ingrese un numero: '))
        while verificarSiEsEntero(i) == False:
            i = int(input('Ingrese un numero: '))
        while i > 0:
            i -= 1
            filas = int(input('Fila del asiento en mal estado: '))
            while verificarSiEsEntero(filas) == False:
                filas = int(input('Fila del asiento en mal estado: '))
            columnas = int(input('Columna del asiento en mal estado: '))
            while verificarSiEsEntero(columnas) == False:
                columnas = int(input('Columna del asiento en mal estado: '))
            asiento_mal_estado = [[filas, columnas]]
            self.mal_estado.append(asiento_mal_estado)
        for ruta in rutas:
            print(f'{rutas.index(ruta)+1}, {ruta.origen} -> {ruta.destino}')
        ruta_bus = int(input('Ruta que seguira el bus: '))
        while verificarSiEsEntero(ruta_bus) == False:
            ruta_bus = int(input('Ruta que seguira el bus: '))
        for ruta in rutas:
            if ruta_bus == rutas.index(ruta)-1:
                ruta_bus = ruta
        self.mostrar_asientos()

    

    def anadir_bus(rutas:list):
        ID_bus = int(input('numero de identificacion del bus: '))
        while verificarSiEsEntero(ID_bus) == False:
            ID_bus = int(input('numero del bus: '))
        placa = input('placa del bus: ')
        conductor = input('conductor del bus: ')
        puestos_mal_estado = int(input('Cantidad de puestos en mal estado: '))
        while verificarSiEsEntero(puestos_mal_estado) == False:
            puestos_mal_estado = int(input('Cantidad de puestos en mal estado: '))
        while puestos_mal_estado > 0:
            asientos_mal_estado = []
            filas = int(input('Fila del asiento en mal estado: '))
            while verificarSiEsEntero(filas) == False:
                filas = int(input('Fila del asiento en mal estado: '))
            columnas = int(input('Columna del asiento en mal estado: '))
            while verificarSiEsEntero(columnas) == False:
                columnas = int(input('Columna del asiento en mal estado: '))
            asientos_mal_estado.append([filas, columnas])
            puestos_mal_estado -= 1
        mal_estado = [asientos for asientos in asientos_mal_estado]
        print(mal_estado)
        for ruta in rutas:
            print(f'{rutas.index(ruta)+1}, {ruta.origen} -> {ruta.destino}')
        ruta_bus = int(input('Ruta que seguira el bus: '))
        while verificarSiEsEntero(ruta_bus) == False:
            ruta_bus = int(input('Ruta que seguira el bus: '))
        for ruta in rutas:
            if ruta_bus == rutas.index(ruta)-1:
                ruta_bus = ruta

        nuevo_bus = Buses(ID_bus, placa, conductor, mal_estado, ruta)
        nuevo_bus.crear_asientos()
        nuevo_bus.asignar_mal_estado()
        nuevo_bus.mostrar_asientos()
        return  nuevo_bus

    
    def crear_asientos(self):
        filas = 4
        columnas = 10
        #asientos libres por defecto
        self.asientos = np.full((filas,columnas), 0, str)
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
        print(self.numero)
        print('0: Libre\n2: Mal estado\n1: Ocupado')
        print(self.asientos)
        print(f'El conductor del bus {self.conductor} atiende en el bus {self.numero} con placa {self.placa}')
        sleep(2)


#hasta aqui vamos bien
class Pasajero:
    def __init__(self, nombre:str, ID:int, edad:int, hora_comprado:int, efectivo:int, puestos:int=0):
        self.nombre = nombre
        self.apellido = ID
        self.edad = edad
        self.hora_comprado = hora_comprado
        self.puestos = puestos
        self.efectivo = efectivo

    
    def anadir_pasajero(self):
        nombre = input('Nombre: ')
        ID = input('ID: ')
        edad = int(input('Edad: '))
        while verificarSiEsEntero(edad) == False:
            edad = int(input('Edad: '))
        hora_comprado = int(input('Hora de compra (Formato 24 horas): '))
        while verificarSiEsEntero(hora_comprado) == False and hora_comprado > 23:
            hora_comprado = int(input('Hora de compra: '))
        efectivo = int(input('Efectivo: '))
        while verificarSiEsEntero(efectivo) == False:
            efectivo = int(input('Efectivo: '))
        nuevo_pasajero = Pasajero(nombre, ID, edad, hora_comprado, efectivo)
        return nuevo_pasajero


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
                bus.asientos_vendidos += 1
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
