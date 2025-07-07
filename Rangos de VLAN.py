def main():
    try:
        vlan = int(input("Ingrese el número de VLAN: "))
        if 1 <= vlan <= 1005:
            print(f"Su VLAN {vlan} se encuentra en el rango estandar (1-1005).")
        elif 1006 <= vlan <= 4094:
            print(f"Su VLAN {vlan} se encuentra en el rango extendido (1006-4094).")
        else:
            print("El número de VLAN ingresado no está en un rango correspondiente (1-4094).")
    except ValueError:
        print("Favor de ingresar un número válido.")

if __name__ == "__main__":
    main()