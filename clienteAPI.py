import json
import requests
opcion=0
while opcion!=7:
    print("Seleccione una opcion")
    print("Web API Bottle - Cliente")
    print("1 - Listar habitaciones ")
    print("2 - Buscar una habitacion por ID ")
    print("3 - Modificar datos de una habitacion")
    print("4 - Dar de alta una nueva habitación")
    print("5 - Consultar habitaciones libres u ocupadas ")
    print("6 - Eliminar una habitación ")
    print("7 - Salir")
    opcion = int(input())
    if opcion==1: #LISTAR
        print("Listar habitaciones:")
        r = requests.get('http://localhost:8080/habitaciones')
        datos=r.json()

        cont = 1
        for k in datos['habitaciones']:
            print("Habitacion",(cont),":")
            cont+=1
            for i in k.keys():
                print(""+str(i)+": "+str(k[i]))
            print("------------------------------")

    elif opcion==2: #BUSCAR POR ID
        print("Buscar por ID de habitacion")
        print("Introduce el ID de habitacion")
        id=input()

        r = requests.get('http://localhost:8080/buscar_habitacion/'+id)
        data = r.json()
        print(data['habitacion'])

    elif opcion==3: #MODIFICAR HABITACION
        print("Modificar habitacion")
        print("Eliga el ID de la habitacion a modificar")
        id=input()
        r = requests.get('http://localhost:8080/buscar_habitacion/'+id)
        data = r.json()
        if data['habitacion']=='Error - ID No encontrado':
            print(data['habitacion'])
        else:
            print(data['habitacion'])
            equipamiento = []
            print("Introduce el numero de plazas:")
            plazas = input()
            print("Cuantos elementos de equipamiento?")
            elementos = int(input())
            for i in range(0, elementos):
                print("Nombre del elemento: ", (i + 1))
                ele = input()
                equipamiento.append(ele)
            print("¿Ocupada? \n 1- Si \n 2- No")
            ocupada = input()
            if ocupada == 1:
                ocupada = True
            else:
                ocupada = False
            modificada = {
                'id': data['habitacion']['ID'],'plazas': plazas, 'equipamiento': equipamiento, 'ocupada': ocupada}
            r = requests.post('http://localhost:8080/mod_habitacion/'+id, json=modificada)
            respuesta = r.json()
            cont = 1
            for k in respuesta['habitaciones']:
                print("Habitacion", (cont), ":")
                for i in k.keys():
                    print("" + str(i) + ": " + str(k[i]))
                print("------------------------------")

    elif opcion==4: #DAR DE ALTA HABITACION
        equipamiento=[]
        print("Dar de alta una habitación")
        print("Introduce el numero de plazas:")
        plazas=input()
        print("¿Ocupada? /n 1- Si /n 2- No")
        ocupada = input()
        if ocupada==1:
            ocupada=True
        else:
            ocupada=False
        print("Cuantos elementos de equipamiento?")
        elementos=int(input())
        for i in range (0,elementos):
            print("Nombre del elemento: ",(i+1))
            ele=input()
            equipamiento.append(ele)
        nueva = {
                'plazas': plazas,
                'equipamiento':equipamiento,
                'ocupada': ocupada}
        r = requests.post('http://localhost:8080/alta_habitacion', json=nueva)
        print("Habitación almacenada")


    elif opcion==5:   # CONSULTAR LIBRES U OCUPADAS

        print("¿Desea consultar habitaciones libres u ocupadas?")
        print("[1] - Libres")
        print("[2] - Ocupadas")
        opcion = input()

        r = requests.get('http://localhost:8080/hab_disponibles/'+opcion)
        datos = r.json()

        cont = 1
        for k in datos['habitaciones']:
            print("Habitacion", (cont), ":")
            cont += 1
            for i in k.keys():
                print("" + str(i) + ": " + str(k[i]))
            print("------------------------------")

    elif opcion==6:  # ELIMINAR
        print("Eliminar habitacion:")
        print("Introduce el ID a eliminar:")
        id=input()
        r = requests.delete('http://localhost:8080/eliminar_habitacion/'+id)
        datos = r.json()
        cont = 1
        for k in datos['habitaciones']:
            print("Habitacion", (cont), ":")
            for i in k.keys():
                print("" + str(i) + ": " + str(k[i]))
            print("------------------------------")




