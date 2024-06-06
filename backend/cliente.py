from backend.hoja_cliente import obtenerHojaDeClientes

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

def consultarCliente(documento):
  refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
  refFilasEnum = enumerate(refFilas)

  for idx, refFila in refFilasEnum:
    if refFila[0].value == documento:
      valores = []
      valores.append(idx)

      for celda in refFila:
        valores.append(celda.value)

      return valores
  else:
    return None
