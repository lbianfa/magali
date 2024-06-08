from utils.terminal import limpiar
import backend.cliente as Cliente
from tabulate import tabulate

headers = ["Número de documento", "Nombre", "Celular", "Ciudad"]

def listarClientes():
  clientes = Cliente.listarClientes()

  print(tabulate(clientes, headers=headers, tablefmt="rounded_grid"))

def consultarCliente():
  documento = input("Ingrese el documento del cliente: ")

  cliente = Cliente.consultarCliente(documento)

  if cliente == None:
    print(f"Cliente con documento {documento} no existe")
    return

  print(tabulate([cliente[1:]], headers=headers, tablefmt="rounded_grid"))

def mostrarMenuDeClientes():
  separador = "----------------------------------------------------"
  bienvenida = "MAGALI"
  opciones = {
    "1": listarClientes,
    "2": consultarCliente,
  }
  solicitud = "Ingrese una opción: "
  salida = False

  while True:
    menu = f"{bienvenida if salida == False else separador}\n1. Listar clientes\n2. Buscar cliente\n3. Salir"
    print(menu)
    opcion = input(solicitud)
    salida = False

    if opcion == "3":
      limpiar()
      break

    if opcion in opciones:
      salida = True
      solicitud = "Ingrese una opción: "
      limpiar()
      opciones.get(opcion)()
    else:
      solicitud = "Opción invalida, ingrese una nueva opción: "
      limpiar()
