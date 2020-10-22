from tkinter import *
from tkinter import ttk
import webbrowser


def abrirFavoritos():
    ######## Ventana favoritos ########
    venFavoritos = Toplevel(root)
    venFavoritos.title("Favoritos")
    venFavoritos.resizable(0, 0)
    venFavoritos.positionfrom()
    venFavoritos.geometry("850x550")
    venFavoritos.transient(root)
    venFavoritos.grab_set()


    ######## Creacion de la lista de favoritos ########
    marcoListaFavoritos = Frame(venFavoritos)
    marcoListaFavoritos.pack()
    marcoListaFavoritos.pack(padx=15, pady=(30, 10))
    listaFavoritos = ttk.Treeview(marcoListaFavoritos, height=20, columns=(0, 1, 2, 3, 4), show="headings")
    listaFavoritos.heading(0, text="ID", anchor=CENTER)
    listaFavoritos.heading(1, text="Categoria", anchor=CENTER)
    listaFavoritos.heading(2, text="Producto", anchor=CENTER)
    listaFavoritos.heading(3, text="Precio", anchor=CENTER)
    listaFavoritos.insert("", END, values=("1", "2", "3", "4"))
    listaFavoritos.insert("", END, values=("2", "1", "4", "3"))
    listaFavoritos.insert("", END, values=("3", "4", "2", "1"))
    listaFavoritos.insert("", END, values=("4", "3", "1", "2"))
    listaFavoritos.column(0, width=40)
    listaFavoritos.column(1, width=150)
    listaFavoritos.column(2, width=400)
    listaFavoritos.column(3, width=140)
    listaFavoritos.column(4, width=0, stretch=NO, minwidth=0)
    listaFavoritos.pack()
    ######## Ordenar lista de favoritos por columna ########
    for col in (0, 1, 2, 3, 4):
        listaFavoritos.heading(col, text=header[col], command=lambda _col=col: ordenar_lista(listaFavoritos, _col, False))


    ######## Creacion de botones de favoritos ########
    marcoBotonesFavoritos = Frame(venFavoritos)
    marcoBotonesFavoritos.pack(padx=12, pady=(10), anchor=CENTER)
    btnLink = Button(marcoBotonesFavoritos, text="Ver en la web", width=13, command=lambda: openweb(listaFavoritos.selection()[4]))
    btnLink.pack(padx=4, side=LEFT, anchor=W)
    btnFav = Button(marcoBotonesFavoritos, text="Borrar de favoritos", width=16, command=lambda: borrarFavorito(listaFavoritos.selection()[0]))
    btnFav.pack(padx=4, side=LEFT, anchor=W)


    ######## Creacion de subtotal ########
    lblSubtotal = Label(marcoBotonesFavoritos, text="Subtotal:")
    lblSubtotal.pack(padx=(200, 2), side=LEFT, anchor=W)
    subtotal = StringVar()
    sumatoria = 0
    for i in listaFavoritos.get_children():
        sumatoria += listaFavoritos.item(i)["values"][3]
    subtotal.set(sumatoria)
    lblCosto = Label(marcoBotonesFavoritos, text="{}".format(subtotal.get()))
    lblCosto.pack(side=RIGHT, anchor=W)


def ordenar_lista(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda _col=col: ordenar_lista(tv, _col, not reverse))


######## Inicializacion ########
header = ("ID", "Categoria", "Producto", "Precio", "")


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
desplegable["values"] = ["Producto", "Categoria"]
buscador = Entry(marcoBuscador, width=50)
buscador.pack(padx=4, side=LEFT, anchor=W)
btnBuscar = Button(marcoBuscador, text="Buscar", width=6, command=lambda: buscarProducto(desplegable.get(), buscador.get()))
btnBuscar.pack(padx=10, side=RIGHT, anchor=W)


######## Creacion de la lista ########
marcoLista = Frame(root)
marcoLista.pack()
marcoLista.pack(padx=15, pady=(0, 10))
style = ttk.Style()
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
lista = ttk.Treeview(marcoLista, height=27, columns=(0, 1, 2, 3, 4), show="headings")
lista.heading(0, text="ID", anchor=CENTER)
lista.heading(1, text="Categoria", anchor=CENTER)
lista.heading(2, text="Producto", anchor=CENTER)
lista.heading(3, text="Precio", anchor=CENTER)
lista.column(0, width=40)
lista.column(1, width=200)
lista.column(2, width=550)
lista.column(3, width=140)
lista.column(4, width=0, stretch=NO, minwidth=0)
lista.insert("", END, values=("1", "2", "3", "4", "www.google....."))
lista.insert("", END, values=("2", "1", "4", "3"))
lista.insert("", END, values=("3", "4", "2", "1"))
lista.insert("", END, values=("4", "3", "1", "2"))
lista.pack()

######## Ordenar lista por columnas ########
for col in (0, 1, 2, 3, 4):
    lista.heading(col, text=header[col], command=lambda _col=col: ordenar_lista(lista, _col, False))


######## Creacion de botones ########
marcoBotones = Frame(root)
marcoBotones.pack(padx=12, pady=(10), anchor=CENTER)
btnLink = Button(marcoBotones, text="Ver en la web", width=13, command=lambda: openweb(lista.selection()[4]))
btnLink.pack(padx=4, side=LEFT, anchor=W)
btnFav = Button(marcoBotones, text="Añadir a favoritos", width=16, command=lambda: agregarFavorito(lista.selection()[0]))
btnFav.pack(padx=4, side=LEFT, anchor=W)



root.mainloop()
