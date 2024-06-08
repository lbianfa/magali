from backend.hoja_cliente import obtenerHojaDeClientes
from backend.excel import guardarHoja

hoja = obtenerHojaDeClientes()

def listarClientes():
  filas = []

  refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)

  for refFila in refFilas:
    valores = []

    for celda in refFila:
      valores.append(celda.value)

    filas.append(valores)

  return filas

def consultarCliente(documento, soloValores = True):
  refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
  refFilasEnum = enumerate(refFilas)

  for idx, refFila in refFilasEnum:
    if refFila[0].value == documento:
      if soloValores:
        valores = []
        valores.append(idx)

        for celda in refFila:
          valores.append(celda.value)

        return valores
      else:
        return refFila
  else:
    return None

def crearCliente(documento, nombre, celular, ciudad):
  if consultarCliente(documento) != None:
    return False

  cliente = (documento, nombre, celular, ciudad)

  hoja.append(cliente)

  guardarHoja(hoja)

  return True

def eliminarCliente(documento):
  cliente = consultarCliente(documento)

  if cliente == None:
    return False

  hoja.delete_rows(cliente[0]+2)

  guardarHoja(hoja)

  return True

def actualizarCliente(documento, nombre, celular, ciudad):
  nuevos_valores = (documento, nombre, celular, ciudad)

  refFila = consultarCliente(documento, False)

  if refFila == None:
    return False

  for celda, nuevo_valor in zip(refFila, nuevos_valores):
    celda.value = nuevo_valor

  guardarHoja(hoja)

  return True
