class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        if not self.cabeza:
            return False

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return True

        actual = self.cabeza
        previo = None
        while actual and actual.dato != dato:
            previo = actual
            actual = actual.siguiente

        if not actual:
            return False

        previo.siguiente = actual.siguiente
        return True
    
    def mostrar(self):
        ingredientes = []
        actual = self.cabeza
        while actual:
            ingredientes.append(actual.dato)
            actual = actual.siguiente
        return ingredientes

POSTRES = {}

def imprimir_ingredientes(postre):
    if postre in POSTRES:
        ingredientes = POSTRES[postre].mostrar()
        if ingredientes:
            print(f"Ingredientes de {postre}: {', '.join(ingredientes)}")
        else:
            print(f"El postre '{postre}' no tiene ingredientes.")
    else:
        print("El postre no existe.")

def agregar_ingrediente(postre, ingrediente):
    if postre in POSTRES:
        POSTRES[postre].agregar(ingrediente)
        print(f"Ingrediente '{ingrediente}' añadido a {postre}.")
    else:
        print("El postre no existe.")

def eliminar_ingrediente(postre, ingrediente):
    if postre in POSTRES:
        eliminado = POSTRES[postre].eliminar(ingrediente)
        if eliminado:
            print(f"Ingrediente '{ingrediente}' eliminado de {postre}.")
        else:
            print(f"El ingrediente '{ingrediente}' no se encontró en {postre}.")
    else:
        print("El postre no existe.")

def alta_postre(postre, ingredientes):
    if postre not in POSTRES:
        POSTRES[postre] = ListaEnlazada()
        for ingrediente in ingredientes:
            POSTRES[postre].agregar(ingrediente)
        print(f"Postre '{postre}' añadido con sus ingredientes.")
    else:
        print("El postre ya existe.")

def baja_postre(postre):
    if postre in POSTRES:
        conservar = input(f"¿Desea conservar los ingredientes de '{postre}'? (s/n): ").strip().lower()
        
        if conservar == 's':
            print(f"Postre '{postre}' eliminado, pero sus ingredientes se han conservado.")
            postre=None
        else:
            del POSTRES[postre]
            print(f"Postre '{postre}' y sus ingredientes han sido eliminados.")
    else:
        print("El postre no existe.")

def eliminar_duplicados():
    for postre, lista in POSTRES.items():
        actual = lista.cabeza
        vistos = set()
        previo = None
        while actual:
            if actual.dato in vistos:
                previo.siguiente = actual.siguiente
            else:
                vistos.add(actual.dato)
                previo = actual
            actual = actual.siguiente
    print("Ingredientes duplicados eliminados.")

def imprimir_todos_los_postres():
    if not POSTRES:
        print("No hay postres disponibles.")
        return
    for postre, lista in POSTRES.items():
        ingredientes = lista.mostrar()
        print(f"{postre}: {', '.join(ingredientes) if ingredientes else 'Sin ingredientes'}")

def mostrar_menu():
    print("\n--- Menú de Gestión de Postres ---")
    print("1. Imprimir la lista de ingredientes de un postre")
    print("2. Agregar un ingrediente a un postre")
    print("3. Eliminar un ingrediente de un postre")
    print("4. Dar de alta un nuevo postre con sus ingredientes")
    print("5. Dar de baja un postre")
    print("6. Eliminar ingredientes duplicados")
    print("7. Imprimir todos los postres")
    print("8. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            postre = input("Ingrese el nombre del postre: ")
            imprimir_ingredientes(postre)
        
        elif opcion == "2":
            postre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el ingrediente a agregar: ")
            agregar_ingrediente(postre, ingrediente)
        
        elif opcion == "3":
            postre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el ingrediente a eliminar: ")
            eliminar_ingrediente(postre, ingrediente)
        
        elif opcion == "4":
            postre = input("Ingrese el nombre del nuevo postre: ")
            ingredientes = input("Ingrese los ingredientes separados por coma: ").split(", ")
            alta_postre(postre, ingredientes)
        
        elif opcion == "5":
            postre = input("Ingrese el nombre del postre a eliminar: ")
            baja_postre(postre)
        
        elif opcion == "6":
            eliminar_duplicados()
        
        elif opcion == "7":
            imprimir_todos_los_postres()
        
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
