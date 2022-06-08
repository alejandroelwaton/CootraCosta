from objects import *

def anadir_bus():
    nombre_bus = input('nombre del bus')
    placa_bus = input('placa del bus')
    conductor_bus = input('conductor del bus')
    mal_estado_bus_int = int(input('mal estado del bus'))
    mal_estado_bus = [mal_estado_bus_int]
    filas_bus = int(input('filas del bus'))
    columnas_bus = int(input('columnas del bus'))

    nuevo_bus = Buses(nombre_bus, placa_bus, conductor_bus, mal_estado_bus, filas_bus, columnas_bus)
    return  nuevo_bus

def main():
    clear()
    sleep(2)
    barranquilla_santa_marta = Rutas('Barranquilla', 'Santa marta', 6, 20000)
    valledupar_monteria = Rutas('Valledupar', 'Monteria', 8, 30000)
    santa_marta_barranquilla = Rutas('Santa marta', 'Barranquilla', 9, 20000)
    cartagena_sincelejo = Rutas('Cartagena', 'Sincelejo', 14, 50000)
    riohacha_monteria = Rutas('Riohacha', 'Monteria', 21, 15000)
    santa_marta_barranquilla_diarias = Rutas('Santa marta', 'Barranquilla', 10, 20000)
    bus = Buses(1, 'ABC123', 'Juan', [[1,2], [2,1]], ruta=valledupar_monteria)

    pasajero3 = Pasajero('juan',3, 19 ,6 , 0, 120000)
    pasajero4 = Pasajero('maria', 4, 18 ,6, 0, 150000)
    bus.crear_asientos()

    bus.mostrar_asientos()
    pasajero3.comprar_asiento(0, 1, bus, valledupar_monteria)
    pasajero4.comprar_asiento(2, 1, bus, valledupar_monteria)
    
    bus.mostrar_asientos()


if __name__ == '__main__':
    main()

