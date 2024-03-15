from Personas import Comprador
from Eventos import EventoParrillada, EventoVIP
from Ventas import Venta, GestorVentas

def realizar_venta(gestor_ventas):
    print("REALIZAR UNA VENTA:")
    nombre_comprador = input("NOMBRE DEL COMPRADOR: ")
    email_comprador = input("EMAIL DEL COMPRADOR: ")
    comprador = Comprador(nombre_comprador, email_comprador)
    
    print("TIPO DE EVENTO:")
    print("1. Parrillada Regular")
    print("2. Parrillada VIP")
    opcion_evento = input("INGRESE EL NUMERO DEL EVENTO (1 O 2): ")

    fecha = input("FECHA DEL EVENTO: ")
    lugar = input("LUGAR DEL EVENTO: ")
    precio = float(input("PRECIO DEL EVENTO: "))

    if opcion_evento == "1":
        evento = EventoParrillada(fecha, lugar, precio)
    elif opcion_evento == "2":
        beneficios = input("Ingrese los beneficios del evento VIP: ")
        evento = EventoVIP(fecha, lugar, precio, beneficios)
    else:
        print("Opción inválida.")
        return
    
    cantidad = int(input("CANTIDAD DE ENTRADAS A VENDER: "))
    venta = Venta(comprador, evento, cantidad)
    gestor_ventas.agregar_venta(venta)
    print("VENTA EXITOSA.")

def reportes_ventas(gestor_ventas):
    print("REPORTES DE VENTAS:")
    print("1. REPORTE POR EVENTOS")
    print("2. REPORTE TOTALES")
    opcion_reporte = input("INGRESE UNA OPCION: ")

    if opcion_reporte == "1":
        print("SELECCIONE UN EVENTO:")
        for index, venta in enumerate(gestor_ventas.ventas, start=1):
            print(f"{index}. {venta.evento.mostrar_detalle()}")
        opcion_evento = int(input("INGRESE UN EVENTO: "))
        evento_seleccionado = gestor_ventas.ventas[opcion_evento - 1].evento
        print(gestor_ventas.reporte_ventas_evento(evento_seleccionado))
    elif opcion_reporte == "2":
        print(gestor_ventas.reporte_ventas_totales())
    else:
        print("Opción inválida.")