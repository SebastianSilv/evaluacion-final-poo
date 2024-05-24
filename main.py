def convertir_caracter_a_bytes(caracter):
    """
    Convierte un caracter en su representacion en bytes.
    """
    # Convertir el caracter a su valor ASCII
    valor_ascii = ord(caracter)
    
    # Convertir el valor ASCII a una cadena de bits
    bits = bin(valor_ascii)[2:].zfill(8)
    
    return bits

def convertir_palabra_a_bytes(palabra):
    """
    Convierte una palabra en su representaciin en bytes.
    """
    bytes_palabra = []
    for caracter in palabra:
        bytes_caracter = convertir_caracter_a_bytes(caracter)
        bytes_palabra.append(bytes_caracter)
    
    return ' '.join(bytes_palabra)

def convertir_bytes_a_caracter(bytes_cadena):
    """
    Convierte una cadena de bytes en su representacion de caracter.
    """
    valor_ascii = int(bytes_cadena, 2)
    caracter = chr(valor_ascii)
    
    return caracter

def menu():
    """
    Muestra el menu de opciones y maneja la ejecucion del programa.
    """
    while True:
        print("\nMenu de opciones:")
        print("1. Convertir un caracter a bytes")
        print("2. Convertir una palabra a bytes")
        print("3. Convertir bytes a caracter")
        print("4. Salir")
        
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            caracter = input("Ingrese un caracter: ")
            bytes_caracter = convertir_caracter_a_bytes(caracter)
            print(f"La representacion en bytes de '{caracter}' es: {bytes_caracter}")
        
        elif opcion == "2":
            palabra = input("Ingrese una palabra: ")
            bytes_palabra = convertir_palabra_a_bytes(palabra)
            print(f"La representacion en bytes de '{palabra}' es: {bytes_palabra}")
        
        elif opcion == "3":
            bytes_cadena = input("Ingrese una cadena de bytes: ")
            caracter = convertir_bytes_a_caracter(bytes_cadena)
            print(f"La representacion de '{bytes_cadena}' es: {caracter} ({ord(caracter)})")
        
        elif opcion == "4":
            print("!Hasta luego!")
            break
        
        else:
            print("Opcion invalida. Intente nuevamente.")

if __name__ == "__main__":
    menu()