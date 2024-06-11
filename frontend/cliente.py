from utils.terminal import limpiar
import backend.cliente as Cliente
from tabulate import tabulate

headers = ["Número de documento", "Nombre", "Celular", "Ciudad"]

def solicitarCliente():
  nombre = input("Ingrese un nombre: ")
  documento = input(f"Ingrese el número de documento de {nombre}: ")
  celular = input(f"Ingrese el celular de {nombre}: ")
  ciudad = input(f"Ingrese la ciudad en donde vive {nombre}: ")

  return (documento, nombre, celular, ciudad)

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

def agregarCliente():
  nuevo_cliente = solicitarCliente()
  cliente_creado = Cliente.crearCliente(*nuevo_cliente)

  if cliente_creado:
    print("Cliente agregado exitosamente...")
  else:
    print("Error agregando el cliente")

def eliminarCliente():
  documento = input("Ingrese el documento del cliente: ")

  cliente_eliminado = Cliente.eliminarCliente(documento)

  if cliente_eliminado:
    print("Cliente eliminado exitosamente...")
  else:
    print("Error: verifique que el cliente con ese documento si exista")

def mostrarMenuDeClientes():
  separador = "----------------------------------------------------"
  bienvenida = "MAGALI"
  opciones = {
    "1": listarClientes,
    "2": consultarCliente,
    "3": agregarCliente,
    "4": eliminarCliente,
  }
  solicitud = "Ingrese una opción: "
  salida = False

  while True:
    menu = f"{bienvenida if salida == False else separador}\n1. Listar clientes\n2. Buscar cliente\n3. Agregar cliente\n4. Eliminar cliente\n5. Salir"
    print(menu)
    opcion = input(solicitud)
    salida = False

    if opcion == "5":
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
