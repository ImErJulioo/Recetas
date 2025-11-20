from collections import namedtuple, List
import csv
from datetime import *

Ingrediente = namedtuple("Ingrediente",
					[("nombre",str),
					 ("cantidad",float),
					 ("unidad",str)])
						 
Receta = namedtuple("Receta", 
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", List[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])

def lee_recetas(fichero):
    with open(fichero, "rt", encoding="utf-8") as f:
        lector =csv.reader(f)
        next(lector)  # Saltar la cabecera
        recetas = []
        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            denominacion = str(denominacion)
            tipo = str(tipo)   
            dificultad = str(dificultad)
            ingredientes = parse_ingredientes(ingredientes)
            tiempo = int(tiempo)
            calorias = int(calorias)
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            precio = float(precio)
            tupla = Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio)
            recetas.append(tupla)
    return recetas

def parse_ingredientes(ingredientes_str):
    ingredientes = []
    ingredientes_list = ingredientes_str.split(";")
    for ingrediente_str in ingredientes_list:
        nombre, cantidad, unidad = ingrediente_str.split(",")
        nombre = str(nombre)
        cantidad = float(cantidad)
        unidad = str(unidad)
        ingrediente = Ingrediente(nombre, cantidad, unidad)
        ingredientes.append(ingrediente)
    return ingredientes
