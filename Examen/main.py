from Interfaz import realizar_venta, reportes_ventas
from Ventas import GestorVentas

def menu_principal():
    print("GESTION DE VENTAS DE TICKETS PARA PARRILLADAS POR EVENTO.")
    print("1). REALIZAR UNA VENTA")
    print("2). MOSTRAR REPORTE DE VENTAS")
    print("3). SALIR")
    opcion = input("INGRESE UNA OPCION: ")
    return opcion

def main():
    gestor_ventas = GestorVentas()
    while True:
        opcion = menu_principal()
        if opcion == "1":
            realizar_venta(gestor_ventas)
        elif opcion == "2":
            reportes_ventas(gestor_ventas)
        elif opcion == "3":
            break
        else:
            print("OPCIÓN INVÁLIDA, INGRESE UNA OPCION VÁLIDA.")

if __name__ == "__main__":
    main()