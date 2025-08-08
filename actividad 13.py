def menu():
    print("=======menu principal======")
    print("1.ingrese cuantos repartidores desea ingresar ")
    print("2. mostrar registro original")
    print("3. ordenar repartidores mostrar posicion")
    print("4. buscar por nombre si aparece en lista")
    print("5. mostrar estadistica general")
    print("6. salir")


class Repartidor:
    def __init__(self, nombre, paquetes, zona):
        if not nombre or not isinstance(nombre):
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if not isinstance(paquetes, int) or paquetes < 0:
            raise ValueError("Los paquetes deben ser un número entero positivo.")
        if not zona:
            raise ValueError("La zona no puede estar vacía.")

        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona

    def __str__(self):
        return f"{self.nombre} - {self.paquetes} paquetes - Zona: {self.zona}"


class EmpresaMensajeria:
    def __init__(self):
        self.repartidores = []

    def agregar_repartidor(self, repartidor):
        if any(r.nombre == repartidor.nombre for r in self.repartidores):
            print(f"Ya existe un repartidor con el nombre '{repartidor.nombre}'. No se agregará.")
        else:
            self.repartidores.append(repartidor)

    def ordenar_por_paquetes(self):
        def quick_sort(lista):
            if len(lista) <= 1:
                return lista
            else:
                pivote = lista[0]
                mayores = [x for x in lista[1:] if x.paquetes > pivote.paquetes]
                iguales = [x for x in lista if x.paquetes == pivote.paquetes]
                menores = [x for x in lista[1:] if x.paquetes < pivote.paquetes]
                return quick_sort(mayores) + iguales + quick_sort(menores)

        self.repartidores = quick_sort(self.repartidores)

    def buscar_repartidor(self, nombre):
        for r in self.repartidores:
            if r.nombre.lower() == nombre.lower():
                return r
        return None

    def mostrar_ranking(self):
        print("\n--- Ranking de Repartidores (mayor a menor paquetes) ---")
        for r in self.repartidores:
            print(r)

    def estadisticas(self):
        if not self.repartidores:
            print("\nNo hay repartidores para mostrar estadísticas.")
            return

        total = sum(r.paquetes for r in self.repartidores)
        promedio = total / len(self.repartidores)
        max_paquetes = max(r.paquetes for r in self.repartidores)
        min_paquetes = min(r.paquetes for r in self.repartidores)

        mejores = [r for r in self.repartidores if r.paquetes == max_paquetes]
        peores = [r for r in self.repartidores if r.paquetes == min_paquetes]

        print("\n--- Estadísticas Generales ---")
        print(f"Total de paquetes entregados: {total}")
        print(f"Promedio de entregas: {promedio:.2f}")
        print("Repartidor(es) con MÁS entregas:")
        for r in mejores:
            print(f" - {r}")
        print("Repartidor(es) con MENOS entregas:")
        for r in peores:
            print(f" - {r}")

empresa = EmpresaMensajeria()

cantidad = int(input("¿Cuántos repartidores desea ingresar? "))

for i in range(cantidad):
    print(f"\nRepartidor #{i + 1}")
    try:
        nombre = input("Ingrese el nombre completo: ")
        paquetes = int(input("Ingrese paquetes entregados: "))
        zona = input("Ingrese zona: ")

        repartidor = Repartidor(nombre, paquetes, zona)
        empresa.agregar_repartidor(repartidor)
    except ValueError as e:
        print(f"Error al ingresar datos: {e}")

print("\n--- Registro Original ---")
for r in empresa.repartidores:
    print(r)

empresa.ordenar_por_paquetes()
empresa.mostrar_ranking()


print("\n--- Búsqueda de Repartidor ---")
nombre_buscar = input("Ingrese el nombre del repartidor a buscar: ")
resultado = empresa.buscar_repartidor(nombre_buscar)
if resultado:
    print(f"Repartidor encontrado: {resultado}")
else:
    print("Repartidor no encontrado.")

empresa.estadisticas()