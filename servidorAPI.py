import json
from random import random, randrange

import bottle
from Scripts.bottle import route, template
from bottle import Bottle, run, get, post, put, request, response

app = Bottle()
print("Cambio en el servidor")
habitaciones = [{'ID': 1, 'Plazas': 3, 'Equipamiento': ['Aire acondicionado', 'Wifi', 'Mini bar'], 'Ocupada': False},
                {'ID': 2, 'Plazas': 4, 'Equipamiento': ['Wifi', 'Caja fuerte', 'Calefaccion'], 'Ocupada': True},
                {'ID': 3, 'Plazas': 5, 'Equipamiento': ['Wifi', 'Armario', 'Calefaccion'], 'Ocupada': False}]


@app.get('/habitaciones')
def get():
    return {'habitaciones': habitaciones}


@app.get('/buscar_habitacion/<id:int>')
def get_by_id(id):
    hab = [hab for hab in habitaciones if hab['ID'] == id]
    if len(hab) == 0:
        return {"habitacion": 'Error - ID No encontrado'}
    else:
        return {'habitacion': hab[0]}


@app.post('/mod_habitacion/<id:int>')
def update(id):
    hab = [hab for hab in habitaciones if hab['ID'] == id]
    if len(hab) == 0:
        return {"Error": "ID No encontrado"}
    else:
        habitaciones.remove(hab[0])
        nueva = {'ID': request.json.get('id'), 'Plazas': request.json.get('plazas'),
                 'Equipamiento': request.json.get('equipamiento'),
                 'Ocupada': request.json.get('ocupada')}
        habitaciones.append(nueva)
        return {'habitaciones': habitaciones}


@app.get('/hab_disponibles/<id:int>')
def get_by_id(id):
    if id == 1:
        disponibilidad = False
    else:
        disponibilidad = True
    hab = [hab for hab in habitaciones if hab['Ocupada'] == disponibilidad]
    return {'habitaciones': hab}


@app.post('/alta_habitacion')
def add():
    estado = True
    while estado == True:  # Genera Ids aleatorios y comprueba si existen
        id = randrange(9999)
        lista_ids = [hab for hab in habitaciones if hab['ID'] == id]
        if len(lista_ids) == 0:
            estado = False

    nueva = {'ID': id, 'Plazas': request.json.get('plazas'), 'Equipamiento': request.json.get('equipamiento'),
             'Ocupada': request.json.get('ocupada')}
    habitaciones.append(nueva)


@app.delete('/eliminar_habitacion/<id:int>')
def remove(id):
    hab = [hab for hab in habitaciones if hab['ID'] == id]
    if len(hab) == 0:
        return {"Error": "ID No encontrado"}
    else:
        habitaciones.remove(hab[0])
        return {'habitaciones': habitaciones}


run(app, host='localhost', port=8080, debug=True, reloader=True)
