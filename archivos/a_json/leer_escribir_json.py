"""
Serializar un objeto, es trasnformar un valor a una determinada estructura de datos en este caso JSON
Deserializar, el proceso inverso
"""

import json

#serializar
json1= json.dumps([1,2,3])
print("json1", json1)

#deserializar
json2 = json.loads('[12,10,33]')
print("json2", json2)


#escribir archivo json  json.dump(valores, archivo)
with open('json_example.txt', 'w') as json_example:
    json.dump([1,200,300], json_example)

# Leer desde json  json.load(archivo_abierto)
with open("json_example.txt", "r") as json_example:
    json.load(json_example)