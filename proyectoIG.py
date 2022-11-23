#!/usr/bin/python3
# IE-0117 Programación Bajo Plataformas Abiertas
# Francisco Moya Mena
# Carnet A74449

import tkinter as tk
from tkinter import ttk


# creamos la ventana principal
ventana = tk.Tk()
ventana.title('Ventana principal')
ventana.geometry('800x600')

# creamos una barra de menús y la añadimos a la ventana principal
# cada ventana solo puede tener una barra de menús
barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)

# creamos un menú cuyo contenedor será la barra de menús
menu = tk.Menu(barra_menus, tearoff=False)


# definimos las acciones asociadas a las opciones de los menús

ListaProducto = [["x"]]
ListaInventario = []


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


def Ingreso():
    INVENTARIO = []
    IngresoProducto = []
    frame = ttk.Frame(ventana)
    frame.pack(side="top", expand=True, fill="both")
    texto = tk.Label(frame, text="Ingreso Producto")
    texto.place(x=300, y=100)
    Codigo_label = tk.Label(frame, text="Codigo Producto")
    Codigo_label.place(x=150, y=200)
    Codigo_entry = ttk.Entry(frame)
    Codigo_entry.pack()
    Codigo_entry.place(x=300, y=200)

    def Codigo_boton():
        Codigo = Codigo_entry.get()
        for bproducto2 in ListaProducto:
            if Codigo == bproducto2[0]:
                producto = 1
                Nombre = bproducto2[1]
                Nombre_label = tk.Label(frame, text="Nombre Producto")
                Nombre_label.place(x=150, y=250)
                Nombre_entry = ttk.Entry(frame)
                Nombre_entry.pack()
                Nombre_entry.place(x=300, y=250)
                Nombre_entry.insert(0, Nombre)                
                break
            else:
                producto = 0
                Nombre_label = tk.Label(frame, text="Nombre Producto")
                Nombre_label.place(x=150, y=250)
                Nombre_entry = ttk.Entry(frame)
                Nombre_entry.pack()
                Nombre_entry.place(x=300, y=250)
                

            Cantidad_label = tk.Label(frame, text="Cantidad Producto")
            Cantidad_label.place(x=150, y=300)
            Cantidad_entry = ttk.Entry(frame)
            Cantidad_entry.pack()
            Cantidad_entry.place(x=300, y=300)
            Precio_label = tk.Label(frame, text="Precio Producto")
            Precio_label.place(x=150, y=350)
            Precio_entry = ttk.Entry(frame)
            Precio_entry.pack()
            Precio_entry.place(x=300, y=350)
            Orden_label = tk.Label(frame, text="Orden Producto")
            Orden_label.place(x=150, y=400)
            Orden_entry = ttk.Entry(frame)
            Orden_entry.pack()
            Orden_entry.place(x=300, y=400)

            def Ingreso_boton():
                Codigo = Codigo_entry.get()                
                Nombre = Nombre_entry.get()
                Cantidad = Cantidad_entry.get()
                Precio = Precio_entry.get()
                Orden = Orden_entry.get()                
                Total = float(Cantidad)*float(Precio)
                if producto == 0:
                    IngresoProducto.append(Codigo)
                    IngresoProducto.append(Nombre)
                    IngresoProducto.append(Cantidad)
                    IngresoProducto.append(Precio)
                    IngresoProducto.append(Total)
                    ListaProducto.append(IngresoProducto)
                    Ingreso_label = tk.Label(frame, text="Ingresado")
                    Ingreso_label.place(x=200, y=500)                    
                else:
                    ActualizarSaldo(Codigo, "I", Cantidad, Total)
                    Actual_label = tk.Label(frame, text="Sistema Actualizado")
                    Actual_label.place(x=200, y=500)                    
                INVENTARIO.append("I")
                INVENTARIO.append(Codigo)
                INVENTARIO.append(Nombre)
                INVENTARIO.append(Cantidad)
                INVENTARIO.append(Precio)
                INVENTARIO.append(Total)
                INVENTARIO.append(Orden)
                ListaInventario.append(INVENTARIO)

        def Return_boton():
            texto = tk.Label(ventana, text="¡Bienvenido a Facturero Python!")
            texto.place(x=300, y=100)
            Codigo_entry.delete(0, "end")
            Nombre_entry.delete(0, "end")
            Cantidad_entry.delete(0, "end")
            Precio_entry.delete(0, "end")
            Orden_entry.delete(0, "end")
            frame.destroy()
        Ingreso_button = ttk.Button(frame, text="Ingresar"
                                    " Producto", command=Ingreso_boton
                                    )
        Ingreso_button.pack()
        Ingreso_button.place(x=500, y=450)
        Return_button = ttk.Button(frame, text="Salir", command=Return_boton
                                   )
        Return_button.pack()
        Return_button.place(x=500, y=500)
    Codigo_button = ttk.Button(frame, text="Buscar"
                               " Codigo", command=Codigo_boton
                               )
    Codigo_button.pack()
    Codigo_button.place(x=500, y=450)


def Egreso():
    INVENTARIO = []
    frame = ttk.Frame(ventana)
    frame.pack(side="top", expand=True, fill="both")
    texto = tk.Label(frame, text="Egreso Producto")
    texto.place(x=300, y=100)
    Codigo_label = tk.Label(frame, text="Codigo Producto")
    Codigo_label.place(x=150, y=200)
    Codigo_entry = ttk.Entry(frame)
    Codigo_entry.pack()
    Codigo_entry.place(x=300, y=200)

    def Codigo_boton():
        bproducto3 = []
        VPRODUCTO = []
        Codigo = Codigo_entry.get()        
        for bproducto3 in ListaProducto:
            if Codigo == bproducto3[0]:
                VPRODUCTO.append(bproducto3[0])
                VPRODUCTO.append(bproducto3[1])
                VPRODUCTO.append(bproducto3[2])
                VPRODUCTO.append(bproducto3[3])
                VPRODUCTO.append(bproducto3[4])
                break
        if len(VPRODUCTO) > 0:
            Nombre = bproducto3[1]
            Nombre_label = tk.Label(frame, text="Nombre Producto")
            Nombre_label.place(x=150, y=250)
            Nombre_entry = ttk.Entry(frame)
            Nombre_entry.pack()
            Nombre_entry.place(x=300, y=250)
            Nombre_entry.insert(0, Nombre)            
            Cantidad_label = tk.Label(frame, text="Cantidad Producto")
            Cantidad_label.place(x=150, y=300)
            Cantidad_entry = ttk.Entry(frame)
            Cantidad_entry.pack()
            Cantidad_entry.place(x=300, y=300)
            Precio = bproducto3[3]
            Precio_label = tk.Label(frame, text="Precio Producto")
            Precio_label.place(x=150, y=350)
            Precio_entry = ttk.Entry(frame)
            Precio_entry.pack()
            Precio_entry.place(x=300, y=350)
            Precio_entry.insert(0, Precio)
            Orden_label = tk.Label(frame, text="Factura Producto")
            Orden_label.place(x=150, y=400)
            Orden_entry = ttk.Entry(frame)
            Orden_entry.pack()
            Orden_entry.place(x=300, y=400)

            def Egreso_boton():
                Nombre = Nombre_entry.get()
                Cantidad = Cantidad_entry.get()
                Precio = Precio_entry.get()
                Orden = Orden_entry.get()               
                Total = float(Cantidad)*float(Precio)
                INVENTARIO.append("E")
                INVENTARIO.append(Codigo)
                INVENTARIO.append(Nombre)
                INVENTARIO.append(Cantidad)
                INVENTARIO.append(float(bproducto3[3]))
                INVENTARIO.append(Total)
                INVENTARIO.append(Orden)
                ActualizarSaldo(Codigo, "E", Cantidad, Total)
                Actual_label = tk.Label(frame, text="Sistema Actualizado")
                Actual_label.place(x=200, y=500)
                ListaInventario.append(INVENTARIO)

            def Return_boton():
                texto = tk.Label(ventana, text="¡Bienvenido"
                                 " a Facturero Python!"
                                 )
                texto.place(x=300, y=100)
                Codigo_entry.delete(0, "end")
                Nombre_entry.delete(0, "end")
                Cantidad_entry.delete(0, "end")
                Precio_entry.delete(0, "end")
                Orden_entry.delete(0, "end")
                frame.destroy()

            Return_button = ttk.Button(frame, text="Salir"
                                       "", command=Return_boton
                                       )
            Return_button.pack()
            Return_button.place(x=500, y=500)
            Egreso_button = ttk.Button(frame, text="Egresar"
                                       " Producto", command=Egreso_boton
                                       )
            Egreso_button.pack()
            Egreso_button.place(x=500, y=450)

        else:
            Egreso_label = tk.Label(frame, text="No Existe")
            Egreso_label.place(x=200, y=500)

        def Return_boton():
            texto = tk.Label(ventana, text="¡Bienvenido"
                             " a Facturero Python!"
                             )
            texto.place(x=300, y=100)
            Codigo_entry.delete(0, "end")
            frame.destroy()

        Return_button = ttk.Button(frame, text="Salir"
                                   "", command=Return_boton
                                   )
        Return_button.pack()
        Return_button.place(x=500, y=500)
    Codigo_button = ttk.Button(frame, text="Buscar"
                               " Codigo", command=Codigo_boton
                               )
    Codigo_button.pack()
    Codigo_button.place(x=500, y=450)


def Inventario():
    frame = ttk.Frame(ventana)
    frame.pack(side="top", expand=True, fill="both")
    texto = tk.Label(frame, text="Inventario Producto")
    texto.place(x=300, y=100)
    Codigo_label = tk.Label(frame, text="Codigo Producto")
    Codigo_label.place(x=150, y=150)
    Codigo_entry = ttk.Entry(frame)
    Codigo_entry.pack()
    Codigo_entry.place(x=300, y=150)

    def Codigo_boton():
        Codigo = Codigo_entry.get()
        for bproducto2 in ListaProducto:
            if Codigo == bproducto2[0]:
                producto = 1
                break
            else:
                producto = 0
        if producto == 0:
            Inventario_label = tk.Label(frame, text="No Existe")
            Inventario_label.place(x=200, y=500)

            def Return_boton():
                texto = tk.Label(ventana, text="¡Bienvenido"
                                 " a Facturero Python!"
                                 )
                texto.place(x=300, y=100)
                Codigo_entry.delete(0, "end")
                frame.destroy()
            Return_button = ttk.Button(frame, text="Salir"
                                       "", command=Return_boton
                                       )
            Return_button.pack()
            Return_button.place(x=500, y=500)
        else:
            for INVENTARIO in ListaInventario:
                if INVENTARIO[1] == Codigo:                    
                    Mov = INVENTARIO[0]
                    Mov_label = tk.Label(frame, text="Movimiento")
                    Mov_label.place(x=150, y=250)
                    Mov_entry = ttk.Entry(frame)
                    Mov_entry.pack()
                    Mov_entry.place(x=300, y=250)
                    Mov_entry.insert("end", Mov)
                    Nombre = INVENTARIO[2]
                    Nombre_label = tk.Label(frame, text="Nombre Producto")
                    Nombre_label.place(x=150, y=200)
                    Nombre_entry = ttk.Entry(frame)
                    Nombre_entry.pack()
                    Nombre_entry.place(x=300, y=200)
                    Nombre_entry.insert(0, Nombre)
                    Cantidad = INVENTARIO[3]
                    Cantidad_label = tk.Label(frame, text="Cantidad Producto")
                    Cantidad_label.place(x=150, y=300)
                    Cantidad_entry = ttk.Entry(frame)
                    Cantidad_entry.pack()
                    Cantidad_entry.place(x=300, y=300)
                    Cantidad_entry.insert("end", Cantidad)
                    Precio = INVENTARIO[4]
                    Precio_label = tk.Label(frame, text="Precio Producto")
                    Precio_label.place(x=150, y=350)
                    Precio_entry = ttk.Entry(frame)
                    Precio_entry.pack()
                    Precio_entry.place(x=300, y=350)
                    Precio_entry.insert("end", Precio)
                    Total = INVENTARIO[5]
                    Total_label = tk.Label(frame, text="Total")
                    Total_label.place(x=150, y=400)
                    Total_entry = ttk.Entry(frame)
                    Total_entry.pack()
                    Total_entry.place(x=300, y=400)
                    Total_entry.insert("end", Total)
                    Orden = INVENTARIO[6]
                    Orden_label = tk.Label(frame, text="Orden Producto")
                    Orden_label.place(x=150, y=450)
                    Orden_entry = ttk.Entry(frame)
                    Orden_entry.pack()
                    Orden_entry.place(x=300, y=450)
                    Orden_entry.insert("end", Orden)

            def Return_boton():
                texto = tk.Label(ventana, text="¡Bienvenido"
                                 " a Facturero Python!"
                                 )
                texto.place(x=300, y=100)
                Codigo_entry.delete(0, "end")
                frame.destroy()
            Return_button = ttk.Button(frame, text="Salir"
                                       "", command=Return_boton
                                       )
            Return_button.pack()
            Return_button.place(x=500, y=500)

    Codigo_button = ttk.Button(frame, text="Buscar"
                               " Codigo", command=Codigo_boton
                               )
    Codigo_button.pack()
    Codigo_button.place(x=500, y=450)


def Informacion():
    frame = ttk.Frame(ventana)
    frame.pack(side="top", expand=True, fill="both")
    texto = tk.Label(frame, text="Información Producto")
    texto.place(x=300, y=100)
    Codigo_label = tk.Label(frame, text="Codigo Producto")
    Codigo_label.place(x=150, y=200)
    Codigo_entry = ttk.Entry(frame)
    Codigo_entry.pack()
    Codigo_entry.place(x=300, y=200)

    def Codigo_boton():
        Codigo = Codigo_entry.get()
        for bproducto2 in ListaProducto:
            if Codigo == bproducto2[0]:
                Codigo = bproducto2[0]
                Nombre = bproducto2[1]
                Nombre_label = tk.Label(frame, text="Nombre Producto")
                Nombre_label.place(x=150, y=250)
                Nombre_entry = ttk.Entry(frame)
                Nombre_entry.pack()
                Nombre_entry.place(x=300, y=250)
                Nombre_entry.insert(0, Nombre)
                Cantidad = bproducto2[2]
                Cantidad_label = tk.Label(frame, text="Cantidad Producto")
                Cantidad_label.place(x=150, y=300)
                Cantidad_entry = ttk.Entry(frame)
                Cantidad_entry.pack()
                Cantidad_entry.place(x=300, y=300)
                Cantidad_entry.insert(0, Cantidad)
                Precio = bproducto2[3]
                Precio_label = tk.Label(frame, text="Precio Producto")
                Precio_label.place(x=150, y=350)
                Precio_entry = ttk.Entry(frame)
                Precio_entry.pack()
                Precio_entry.place(x=300, y=350)
                Precio_entry.insert(0, Precio)
                Total = bproducto2[4]
                Total_label = tk.Label(frame, text="Total")
                Total_label.place(x=150, y=400)
                Total_entry = ttk.Entry(frame)
                Total_entry.pack()
                Total_entry.place(x=300, y=400)
                Total_entry.insert(0, Total)
                break
            else:
                Informacion_label = tk.Label(frame, text="No Existe")
                Informacion_label.place(x=200, y=500)

        def Return_boton():
            texto = tk.Label(ventana, text="¡Bienvenido"
                             " a Facturero Python!"
                             )
            texto.place(x=300, y=100)
            Codigo_entry.delete(0, "end")
            frame.destroy()

        Return_button = ttk.Button(frame, text="Salir"
                                   "", command=Return_boton
                                   )
        Return_button.pack()
        Return_button.place(x=500, y=500)
    Codigo_button = ttk.Button(frame, text="Buscar"
                               " Codigo", command=Codigo_boton
                               )
    Codigo_button.pack()
    Codigo_button.place(x=500, y=450)

# añadimos opciones al menú indicando su nombre y acción asociado


menu.add_command(label='Ingreso Producto', command=Ingreso)
menu.add_command(label='Egreso Producto', command=Egreso)
menu.add_command(label='Inventario Producto', command=Inventario)
menu.add_command(label='Información Producto', command=Informacion)


# añadimos una línea separadora y la opción de salir
menu.add_separator()
menu.add_command(label='Salir', command=ventana.destroy)

# finalmente añadimos el menú a la barra de menús
barra_menus.add_cascade(label="Menú", menu=menu)

# añadimos una etiqueta para ver el efecto de los botones del menú
texto = tk.Label(ventana, text='¡Bienvenido a Facturero Python!')
texto.place(x=300, y=100)


if __name__ == '__main__':
    ventana.mainloop()  # ejecutamos la ventana principal
