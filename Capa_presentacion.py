from tkinter import *
from tkinter import ttk
import webbrowser


def abrirFavoritos():
    venFavoritos = Toplevel(root)
    venFavoritos.title("Favoritos")
    venFavoritos.resizable(0, 0)
    venFavoritos.positionfrom()
    venFavoritos.geometry("850x600")
    venFavoritos.transient(root)
    venFavoritos.grab_set()

    ######## Ventana favoritos ########
    marcoFavoritos = Frame(venFavoritos)
    marcoFavoritos.pack()
    #marcoFavoritos.config(width="190", height="290")
    marcoFavoritos.config(bd=2)
    marcoFavoritos.pack(pady=5, padx=5)

    marcoFavoritos = Frame(venFavoritos)
    marcoFavoritos.pack(padx=10, pady=(20, 20), side=TOP, anchor=CENTER)


    ######## Creacion de la lista de favoritos ########
    marcoListaFavoritos = Frame(venFavoritos)
    marcoListaFavoritos.pack()
    marcoListaFavoritos.pack(padx=15, pady=(0, 10))
    tablaFavoritos = ttk.Treeview(marcoListaFavoritos, height=20, columns=(0, 1, 2, 3, 4), show="headings")
    tablaFavoritos.heading(0, text="ID", anchor=CENTER)
    tablaFavoritos.heading(1, text="Categoria", anchor=CENTER)
    tablaFavoritos.heading(2, text="Producto", anchor=CENTER)
    tablaFavoritos.heading(3, text="Precio", anchor=CENTER)
    tablaFavoritos.column(0, width=40)
    tablaFavoritos.column(1, width=150)
    tablaFavoritos.column(2, width=400)
    tablaFavoritos.column(3, width=140)
    tablaFavoritos.column(4, width=0)
    tablaFavoritos.pack()


    ######## Creacion de subtotal ########
    marcoCostoFavoritos = Frame(venFavoritos)
    marcoCostoFavoritos.pack(padx=12, pady=(10), anchor=CENTER)
    lblCosto = Label(marcoCostoFavoritos, text="Subtotal:")
    lblCosto.pack(padx=4, side=LEFT, anchor=W)
    subtotal = StringVar()
    sumatoria = 0
    for i in tablaFavoritos.get_children():
        sumatoria += tablaFavoritos.item(i)["values"][3]
    subtotal.set(sumatoria)
    lblSubtotal = Label(marcoCostoFavoritos, text="{}".format(subtotal.get()))
    lblSubtotal.pack(padx=4, side=RIGHT, anchor=W)



######## Creacion del root ########
root = Tk()
root.title("UTN Tecno")
root.geometry("1050x720")
root.resizable(0, 0)


######## Creacion del buscador ########
marcoBuscador = Frame(root)
marcoBuscador.pack(padx=10, pady=(20, 20), side=TOP, anchor=CENTER)
btnFavoritos = Button(marcoBuscador, text="Favoritos", width=8, command=lambda: abrirFavoritos())
btnFavoritos.pack(padx=10, side=RIGHT, anchor=W)
desplegable = ttk.Combobox(marcoBuscador, state="readonly", width=20)
desplegable.pack(padx=4, side=LEFT, anchor=W)
desplegable["values"] = ["Producto", "Categoria", "Mayor precio", "Menor precio"]
buscador = Entry(marcoBuscador, width=50)
buscador.pack(padx=4, side=LEFT, anchor=W)
btnBuscar = Button(marcoBuscador, text="Buscar", width=6, command=lambda: buscarProducto(desplegable.get(), buscador.get()))
btnBuscar.pack(padx=10, side=RIGHT, anchor=W)


######## Creacion de la lista ########
marcoLista = Frame(root)
marcoLista.pack()
marcoLista.pack(padx=15, pady=(0, 10))
tabla = ttk.Treeview(marcoLista, height=27, columns=(0, 1, 2, 3, 4), show="headings")
tabla.heading(0, text="ID", anchor=CENTER)
tabla.heading(1, text="Categoria", anchor=CENTER)
tabla.heading(2, text="Producto", anchor=CENTER)
tabla.heading(3, text="Precio", anchor=CENTER)
tabla.column(0, width=40)
tabla.column(1, width=200)
tabla.column(2, width=550)
tabla.column(3, width=140)
tabla.column(4, width=0)
tabla.pack()


######## Creacion de botones ########
marcoBotones = Frame(root)
marcoBotones.pack(padx=12, pady=(10), anchor=CENTER)
btnLink = Button(marcoBotones, text="Ver en la web", width=13, command=lambda: openweb(tabla.selection()[4]))
btnLink.pack(padx=4, side=LEFT, anchor=W)
btnFav = Button(marcoBotones, text="Añadir a favoritos", width=16, command=lambda: agregarFavorito(tabla.selection()[0]))
btnFav.pack(padx=4, side=LEFT, anchor=W)



root.mainloop()
