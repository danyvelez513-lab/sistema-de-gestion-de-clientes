import collections
from collections import OrderedDict

#listas con los datos de clientes

compras = [
    "Luis", "Chloe", "Ana", "Luis", "Carlos", "Marta", "Sofia", "Noah", "Chloe",
    "Ana", "Sofía", "Chloe", "Elena", "Luis", "Carlos", "Maria", "Juan", "Sofia", "Chloe"
]

registrados = [
    "Ana", "Carlos", "Marta", "Elena", "Noah", "Sofia"
]

#clientes nuevos 

def obtener_clientes_nuevos(compras, registrados):
    conjunto_compras = set(compras) #convierte la lista en un conjunto y elimina duplicados
    conjunto_registrados = set(registrados)
    return list(conjunto_compras.difference(conjunto_registrados))


#Clientes únicos

def obtener_clientes_unicos(compras):
    return list(OrderedDict.fromkeys(compras))  #orderdirect para eliminar los duplicados pero mantener el orden original

#contar compras automaticamente con counter

def contar_compras(compras):
    return collections.Counter(compras)


#filtrar clientes frecuentes

def filtrar_frecuentes(conteo):
    return {
        cliente: veces
        for cliente, veces in conteo.items()
        if veces > 1
    }


#crear resumen personalizado

def crear_resumen(frecuentes):
    return {
        cliente: f"Ha comprado {veces} veces"
        for cliente, veces in frecuentes.items()
    }


#llama a cada funcion, cada variable guardo los resultados de una funcion e imprime los resultados

def main():
    nuevos = obtener_clientes_nuevos(compras, registrados)
    unicos = obtener_clientes_unicos(compras)
    conteo = contar_compras(compras)
    frecuentes = filtrar_frecuentes(conteo)
    resumen = crear_resumen(frecuentes)

    print("Clientes nuevos no registrados:")
    print(nuevos)

    print("\nClientes únicos:")
    print(unicos)

    print("\nResumen por cliente frecuente:")
    for cliente, mensaje in resumen.items():
        print(f"{cliente}: {mensaje}")

#ejecuta main
if __name__ == "__main__":
    main()