from typing import NamedTuple
from typing import List
import csv
from datetime import *

Ingrediente = NamedTuple("Ingrediente",
					[("nombre",str),
					 ("cantidad",float),
					 ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
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
        lector =csv.reader(f, delimiter=";")
        next(lector)  # Saltar la cabecera
        recetas = []
        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            denominacion = str(denominacion)
            tipo = str(tipo)   
            dificultad = str(dificultad)
            ingredientes = parsea_ingredientes(ingredientes)
            tiempo = int(tiempo)
            calorias = int(calorias)
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            precio = float(precio.replace(",","."))
            tupla = Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio)
            recetas.append(tupla)
    return recetas

def parsea_ingredientes(ingredientes_str):
    # Si está vacío → no hay ingredientes
    if not ingredientes_str.strip():
        return []

    lista = []
    ingredientes_raw = ingredientes_str.split(",")

    for ingrediente_str in ingredientes_raw:
        ing = parsea_ingrediente(ingrediente_str)
        if ing is not None:   # por si hay algún ingrediente vacío
            lista.append(ing)

    return lista


def parsea_ingrediente(ingrediente_str):
    ingrediente_str = ingrediente_str.strip()

    if ingrediente_str == "":
        return None

    nombre, cantidad, unidad = ingrediente_str.split("-")
    return Ingrediente(nombre, float(cantidad), unidad)



def ingredientes_en_unidad(recetas: list[Receta], unidad: str | None = None) -> int:
    ingredientes_unicos = set()
    for receta in recetas:
        for ing in receta.ingredientes:
            if unidad is None or ing.unidad == unidad:
                ingredientes_unicos.add(ing.nombre)
    return len(ingredientes_unicos)

def recetas_con_ingredientes(recetas:list[Receta], nombres_ingredientes:set):
    res=[]
    for receta in recetas:
        for nombres_ingrediente in nombres_ingredientes:
            if any(ing.nombre == nombres_ingrediente for ing in receta.ingredientes):
                tupla=(receta.denominacion, receta.calorias, receta.precio)
                res.append(tupla)
    return res

def receta_mas_barata(recetas:list[Receta], tipos_receta:set, n:int | None = None):
    res=[]
    for receta in recetas:
        if receta.tipo in tipos_receta:
                res.append(receta)
    sorted_res = sorted(res, key=lambda x: x[5])
    if n==None or n==1:
        return min(sorted_res, key=lambda x:x[7])
    else:
        lista_capada = sorted_res[:n]
        return min(lista_capada, key=lambda x:x[7])
    
def recetas_baratas_con_menos_calorias(recetas:list[Receta], n):
    res=[]
    reso=[]
    suma=0
    for receta in recetas:
        suma +=receta.precio
    precio_medio = suma/len(recetas)
    for receta in recetas:
        if precio_medio>receta.precio:
            res.append(receta)
    sorted_res:list[Receta] = sorted(res, key=lambda x: x[5])
    for sr in sorted_res:
        tupla = (sr.denominacion, sr.calorias)
        reso.append(tupla)
    return reso[:n]