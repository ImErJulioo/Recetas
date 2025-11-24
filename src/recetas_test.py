from recetas import *

def test_lee_recetas(fichero):
    print("Registros leídos: ", len(lee_recetas(fichero)))
    print("Los dos primeros: ",lee_recetas(fichero)[:2], "\n")
    print("Los dos últimos: ",lee_recetas(fichero)[-2:])

def test_ingredientes_en_unidad(fichero, unidad=None):
    if unidad==None:
        print(f"\nHay ", ingredientes_en_unidad(fichero, unidad), " ingredientes distintos que se miden en None.")
    else:
        print(f"\nHay ", ingredientes_en_unidad(fichero, unidad), " ingredientes distintos que se miden en " + unidad + ".")

def test_recetas_con_ingredientes(recetas:list[Receta], nombres_ingredientes:set):
    print(f"\nLas recetas con alguno de los siguiente ingredientes {nombres_ingredientes} son:")
    print(recetas_con_ingredientes(recetas, nombres_ingredientes))

def test_receta_mas_barata(recetas:list[Receta], tipos_receta:set, n:int | None = None):
    if n==1 or n==None:
        print(f"\nLa receta más barata de alguno de los siguientes tipos {tipos_receta} es:")
        print(receta_mas_barata(lee_recetas(fichero), tipos_receta, n))
    else:
        print(f"\nLa receta más barata de alguno de los siguientes tipos {tipos_receta} entre las {n} con menos calorías es:")
        print(receta_mas_barata(lee_recetas(fichero), tipos_receta, n))

def test_recetas_baratas_con_menos_calorias(fichero, n):
    print(f"\n Las {n} recetas con menos calorías con precio menor que el promedio son:")
    lista=(recetas_baratas_con_menos_calorias(lee_recetas(fichero), n))
    for lis in lista:
        print(lis)

if __name__ == "__main__":
    fichero = 'data/recetas.csv'
    test_lee_recetas(fichero)
    test_ingredientes_en_unidad(lee_recetas(fichero), "gr")
    test_recetas_con_ingredientes(lee_recetas(fichero), {"harina", "azúcar"})
    test_receta_mas_barata(lee_recetas(fichero), {'Postre','Plato principal'}, 5)
    test_recetas_baratas_con_menos_calorias(fichero, 5)