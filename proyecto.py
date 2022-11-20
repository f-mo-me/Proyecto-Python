#!/usr/bin/python3
# IE-0117 Programación Bajo Plataformas Abiertas
# Francisco Moya Mena
# Carnet A74449

if __name__ == '__main__':

    ListaProducto = ["0"]
    ListaInventario = []


# Se busca el producto, si no está se ingresa y si está se actualiza


def BuscarProducto(Codigo):
    for bproducto in ListaProducto:
        if Codigo == bproducto[0]:
            producto = 1
            break
        else:
            producto = 0
    return producto

# Se busca el nombre del producto, si no está se ingresa y si está se actualiza


def BuscarProducto2(Codigo):
    for bproducto2 in ListaProducto:
        if Codigo == bproducto2[0]:
            Nombre = bproducto2[1]
            break
        else:
            Nombre = ""
    return Nombre

# Se extraen todos los datos del producto a buscar


def BuscarProducto3(Codigo):
    VPRODUCTO = []
    for bproducto3 in ListaProducto:
        if Codigo in bproducto3[0]:
            VPRODUCTO.append(bproducto3[0])
            VPRODUCTO.append(bproducto3[1])
            VPRODUCTO.append(bproducto3[2])
            VPRODUCTO.append(bproducto3[3])
            VPRODUCTO.append(bproducto3[4])
    return VPRODUCTO

# Se muestran los datos del producto a buscar


def BuscarProducto4(Codigo):
    for bproducto4 in ListaProducto:
        if Codigo in bproducto4[0]:
            print("\nCodigo: ", bproducto4[0])
            print("Nombre: ", bproducto4[1])
            print("Saldo Disponible: ", bproducto4[2])
            print("Precio Unitario: ", bproducto4[3])
            print("Total: ", bproducto4[4])

# Se actualiza el Saldo del producto de acuerdo al movimiento (Ingreso/Egreso)


def ActualizarSaldo(Codigo, TipoMov, Cantidad, Total):
    VPRODUCTO2 = []
    for bproducto5 in ListaProducto:
        if Codigo in bproducto5[0]:
            ListaProducto.remove(bproducto5)
            CantidadT = float(bproducto5[2])
            TotalT = float(bproducto5[4])
            if TipoMov == "I":
                CantidadT = CantidadT+float(Cantidad)
                TotalT = TotalT+float(Total)
                print("\nSistema Actualizado")
                print("Cantidad Disponible:", CantidadT)
                print("Saldo Actual", TotalT)
                Costo = TotalT/CantidadT
                VPRODUCTO2.append(bproducto5[0])
                VPRODUCTO2.append(bproducto5[1])
                VPRODUCTO2.append(CantidadT)
                VPRODUCTO2.append(Costo)
                VPRODUCTO2.append(TotalT)
                ListaProducto.append(VPRODUCTO2)
                break
            else:
                CantidadT = CantidadT-float(Cantidad)
                TotalT = TotalT-float(Total)
                print("\nSistema Actualizado")
                print("Cantidad Disponible:", CantidadT)
                print("Saldo Actual:", TotalT)
            if CantidadT == 0:
                Costo = 0
            else:
                Costo = TotalT/CantidadT
            VPRODUCTO2.append(bproducto5[0])
            VPRODUCTO2.append(bproducto5[1])
            VPRODUCTO2.append(CantidadT)
            VPRODUCTO2.append(Costo)
            VPRODUCTO2.append(TotalT)
            ListaProducto.append(VPRODUCTO2)
            break

# Se realiza el ingreso de producto


def Ingreso():
    INVENTARIO = []
    IngresoProducto = []
    print("\n****** INGRESO DE PRODUCTO ******\n")
    Codigo = input("Ingrese el Código del Producto: ")
    Nombre = BuscarProducto2(Codigo)
    if Nombre == "":
        Nombre = input("\nIngrese Nombre del Producto: ")
    else:
        Nombre = BuscarProducto2(Codigo)
        print("\nNombre del Producto: ", Nombre)
    Cantidad = float(input("Ingrese la Cantidad del Producto: "))
    Precio = float(input("Ingrese el Precio Unitario: "))
    Total = Cantidad*Precio
    Orden = input("Ingrese el Código de Orden de Compra: ")
    if BuscarProducto(Codigo) == 0:
        IngresoProducto.append(Codigo)
        IngresoProducto.append(Nombre)
        IngresoProducto.append(Cantidad)
        IngresoProducto.append(Precio)
        IngresoProducto.append(Total)
        ListaProducto.append(IngresoProducto)
        print("\nIngresado")
    else:
        ActualizarSaldo(Codigo, "I", Cantidad, Total)
    INVENTARIO.append("I")
    INVENTARIO.append(Codigo)
    INVENTARIO.append(Nombre)
    INVENTARIO.append(Cantidad)
    INVENTARIO.append(Precio)
    INVENTARIO.append(Total)
    INVENTARIO.append(Orden)
    ListaInventario.append(INVENTARIO)

# Se realiza el egreso de producto


def Egreso():
    INVENTARIO = []
    EgresoProducto = []
    print("\n****** EGRESO DE PRODUCTO ******\n")
    Codigo = input("Ingrese el Código del Producto: ")
    EgresoProducto = BuscarProducto3(Codigo)
    if len(EgresoProducto) > 0:
        print("\nNombre del Producto: ", EgresoProducto[1])
        print("Costo del Producto: ", EgresoProducto[3])
        Cantidad = float(input("Ingrese la Cantidad a Egresar: "))
        Total = float(EgresoProducto[3])*Cantidad
        Orden = input("Ingrese el Código de Factura: ")
        INVENTARIO.append("E")
        INVENTARIO.append(Codigo)
        INVENTARIO.append(EgresoProducto[1])
        INVENTARIO.append(Cantidad)
        INVENTARIO.append(float(EgresoProducto[3]))
        INVENTARIO.append(Total)
        INVENTARIO.append(Orden)
        ActualizarSaldo(Codigo, "E", Cantidad, Total)
        ListaInventario.append(INVENTARIO)
    else:
        print("\nCódigo No Existe")

# Se muestra el inventario de un producto


def Inventario():
    INVENTARIO = []
    print("\n****** INVENTARIO DE PRODUCTO ******\n")
    Codigo = input("Ingrese el Código del Producto: ")
    if BuscarProducto(Codigo) == 0:
        print("\nCódigo No Existe")
    else:
        print(
              "{:>8} {:>11} {:>10} {:>12} {:>12} {:>15}"
              "{:>15}".format(
                              "\nMOVIMIENTO", "CODIGO", "NOMBRE", "CANTIDAD",
                              "COSTO", "TOTAL", "DOCUMENTO"
                              ))
        for INVENTARIO in (ListaInventario):
            if INVENTARIO[1] == Codigo:
                MOVIMIENTO, CODIGO, NOMBRE, CANTIDAD, COSTO, TOTAL, DOCUMENTO = INVENTARIO
                print(
                      "{:>10} {:>11} {:>10} {:>12} {:>12} {:>15}"
                      "{:>15}".format(MOVIMIENTO, CODIGO, NOMBRE, CANTIDAD,
                                      COSTO, TOTAL, DOCUMENTO
                                      ))

# Menú Principal


while True:
    print("\n<<<SISTEMA DE INVENTARIO>>>\n")
    print("****** MENU PRINCIPAL ******\n")
    print("1. INGRESO DE PRODUCTO")
    print("2. EGRESO DE PRODUCTO")
    print("3. INVENTARIO")
    print("4. INFORMACION DE PRODUCTO")
    print("0. SALIR")
    opcion = input("\nDigitar una Opción: ")
    if opcion == "0":
        break
    elif opcion == "1":
        Ingreso()
    elif opcion == "2":
        Egreso()
    elif opcion == "3":
        Inventario()
    elif opcion == "4":
        print("\n****** INFORMACION DE PRODUCTO ******\n")
        Codigo = input("Ingrese el Código del Producto: ")
        BuscarProducto4(Codigo)
    else:
        print("\nOpción no válida")
