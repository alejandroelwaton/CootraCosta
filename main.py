from objects import *



barranquilla_santa_marta = Rutas('Barranquilla', 'Santa marta', 6, 20000)
valledupar_monteria = Rutas('Valledupar', 'Monteria', 8, 30000)
santa_marta_barranquilla = Rutas('Santa marta', 'Barranquilla', 9, 20000)
cartagena_sincelejo = Rutas('Cartagena', 'Sincelejo', 14, 50000)
riohacha_monteria = Rutas('Riohacha', 'Monteria', 21, 15000)
santa_marta_barranquilla_diarias = Rutas('Santa marta', 'Barranquilla', 10, 20000)
rutas = [barranquilla_santa_marta, valledupar_monteria, santa_marta_barranquilla, cartagena_sincelejo, riohacha_monteria, santa_marta_barranquilla_diarias]
buses = []
pasajeros = []

def main():
    bus = Buses(1, 'ABS', 'Fuena', [[2,2]], barranquilla_santa_marta)
    print('Bienvenido a Cootracosta')

    while True:
        inicio_del_programa = int(input('''
1. Crear un nuevo bus
2. Modificar un bus
3. Mostrar buses
4. Mostrar rutas
5. Crear ruta
6. Modificar ruta
7. Crear pasajero
8. Mostrar pasajeros
9. Comprar pasaje

'''))
        if inicio_del_programa == 1:
            nuevo_bus = Buses.anadir_bus(rutas)
            buses.append(nuevo_bus)
        
        elif inicio_del_programa == 2:
            if len(buses) == 0:
                print('No hay buses creados')
            else:
                for bus in buses:
                    print(f'{buses.index(bus)+1}, {bus.numero}')
                    bus_a_modificar = int(input('Bus a modificar: '))
                    if bus_a_modificar == buses.index(bus)+1:
                        bus.modificar_bus(rutas)
        
        elif inicio_del_programa == 3:
            if len(buses) == 0:
                print('No hay buses creados')
            else:
                for bus in buses:
                    print(f'{buses.index(bus)+1}, {bus.numero}')
        
        elif inicio_del_programa == 4:
            if len(rutas) == 0:
                print('No hay rutas creadas')
            else:
                for ruta in rutas:
                    print(f'{rutas.index(ruta)+1}, {ruta.origen} - {ruta.destino}')
        
        elif inicio_del_programa == 5:
            nueva_ruta = Rutas.anadir_ruta(rutas)
            rutas.append(nueva_ruta)
        
        elif inicio_del_programa == 6:
            if len(rutas) == 0:
                print('No hay rutas creadas')
            else:
                for ruta in rutas:
                    print(f'{rutas.index(ruta)+1}, {ruta.origen} - {ruta.destino}')
                ruta_a_modificar = int(input('Ruta a modificar: '))
                if ruta_a_modificar == rutas.index(ruta)+1:
                    ruta.modificar_ruta(rutas)
        
        elif inicio_del_programa == 7:
            nuevo_pasajero = Pasajero.anadir_pasajero(Pasajero)
            pasajeros.append(nuevo_pasajero)

        elif inicio_del_programa == 8:
            if len(pasajeros) == 0:
                print('No hay pasajeros creados')
            else:
                for pasajero in pasajeros:
                    print(f'{pasajeros.index(pasajero)+1}, {pasajero.nombre}')
        
        elif inicio_del_programa == 9:
            if len(pasajeros) == 0:
                print('No hay pasajeros creados')
            else:
                for pasajero in pasajeros:
                    print(f'{pasajeros.index(pasajero)+1}, {pasajero.nombre}')
                pasajero_a_comprar = int(input('Pasajero a comprar: '))
                for i in pasajeros:
                    if pasajero_a_comprar == pasajeros.index(i)-1:
                        i = i
                    print(pasajero_a_comprar)
                    fila = int(input('Fila: '))
                    columna = int(input('Columna: '))
                    for i in buses:
                        print('No hay buses disponibles' if len(buses) == 0 else buses.index(i)+1, i.numero)
                    bus_a_comprar = int(input('Bus a comprar: '))
                    for i in buses:
                        if bus_a_comprar == buses.index(i)-1:
                            bus_a_comprar = i
                    for i in rutas:
                        print('No hay rutas disponibles' if len(rutas) == 0 else rutas.index(i)+1, i.origen, i.destino)
                    ruta = int(input('Ruta a comprar: '))
                    for i in rutas:
                        if ruta == rutas.index(i)-1:
                            ruta = i
                    i.comprar_asiento(fila, columna, ruta, bus_a_comprar)
        



if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('TRATO DE CERRAR EL PROGRAMA')

