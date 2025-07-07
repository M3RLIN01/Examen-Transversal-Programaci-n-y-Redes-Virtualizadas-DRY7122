import openrouteservice
import sys

API_KEY = "5b3ce3597851110001cf6248a363eb175f694dc0b4b8c7ac1edd2a0f"
client = openrouteservice.Client(key=API_KEY)

def coordenadas(ciudad):
    r = client.pelias_search(text=ciudad)
    f = r['features'][0]
    return f['geometry']['coordinates'], f['properties']['country']

def ruta(origen, destino, medio):
    return client.directions(
        coordinates=[origen, destino],
        profile=medio,
        format='geojson',
        instructions=True,
        language='es'  
    )

print("=== EXAMEN TRANSVERSAL PROGRAMACION DE REDES VIRTUALIZADAS ===")
print("--- Ítem 2: Geolocalización ---")
print("Solo válido entre ciudades de Chile y Argentina.")
print("Escriba 's' para salir en cualquier momento.\n")

while True:
    o = input("Ciudad de origen: ")
    if o.lower() == 's': sys.exit()
    d = input("Ciudad de destino: ")
    if d.lower() == 's': sys.exit()
    m = input("Tipo de transporte (auto: driving-car, bicicleta: cycling-regular, a pie: foot-walking): ")
    if m.lower() == 's': sys.exit()

    coo_o, pais_o = coordenadas(o)
    coo_d, pais_d = coordenadas(d)

    if pais_o not in ['Chile', 'Argentina'] or pais_d not in ['Chile', 'Argentina']:
        print("Error: Solo se permiten ciudades de Chile o Argentina.\n")
        continue

    rta = ruta(coo_o, coo_d, m)
    seg = rta['features'][0]['properties']['segments'][0]['duration']
    km = rta['features'][0]['properties']['segments'][0]['distance'] / 1000
    mi = km * 0.621371

    h, m, s = int(seg//3600), int((seg%3600)//60), int(seg%60)
    print(f"\nDistancia: {km:.2f} km ({mi:.2f} millas)")
    print(f"Duración estimada: {h}h {m}m {s}s\n")
    print("Instrucciones del viaje:")
    for paso in rta['features'][0]['properties']['segments'][0]['steps']:
        print("-", paso['instruction'])
    print()