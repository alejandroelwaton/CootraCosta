from objects import *



barranquilla_santa_marta = Rutas('Barranquilla', 'Santa marta', 6, 20000)
valledupar_monteria = Rutas('Valledupar', 'Monteria', 8, 30000)
santa_marta_barranquilla = Rutas('Santa marta', 'Barranquilla', 9, 20000)
cartagena_sincelejo = Rutas('Cartagena', 'Sincelejo', 14, 50000)
riohacha_monteria = Rutas('Riohacha', 'Monteria', 21, 15000)
santa_marta_barranquilla_diarias = Rutas('Santa marta', 'Barranquilla', 10, 20000)
rutas = [barranquilla_santa_marta, valledupar_monteria, santa_marta_barranquilla, cartagena_sincelejo, riohacha_monteria, santa_marta_barranquilla_diarias]
buses = []

def main():
    clear()
    sleep(2)
    print('Bienvenido a Cootracosta')

    while True:
        inicio_del_programa = int(input('''
1. Crear un nuevo bus
2. Modificar un bus
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



if __name__ == '__main__':
    main()

