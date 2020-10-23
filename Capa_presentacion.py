from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import messagebox
from Capa_negocio import ArticulosBusiness


def abrirFavoritos():
    ######## Ventana favoritos ########
    venFavoritos = Toplevel(root)
    venFavoritos.title("Favoritos")
    venFavoritos.resizable(0, 0)
    venFavoritos.positionfrom()
    venFavoritos.geometry("850x350")
    venFavoritos.transient(root)
    venFavoritos.grab_set()


    ######## Creacion de la lista de favoritos ########
    marcoListaFavoritos = Frame(venFavoritos)
    marcoListaFavoritos.pack()
    marcoListaFavoritos.pack(padx=15, pady=(30, 10))
    scrollbarFavoritos = Scrollbar(marcoListaFavoritos, orient ="vertical")
    scrollbarFavoritos.pack(side=RIGHT, fill="y")
    listaFavoritos = ttk.Treeview(marcoListaFavoritos, height=11, columns=(0, 1, 2, 3, 4), show="headings")
    listaFavoritos.heading(0, text="ID", anchor=CENTER)
    listaFavoritos.heading(1, text="Categoria", anchor=CENTER)
    listaFavoritos.heading(2, text="Producto", anchor=CENTER)
    listaFavoritos.heading(3, text="Precio", anchor=CENTER)
    listaFavoritos.column(0, width=40)
    listaFavoritos.column(1, width=150)
    listaFavoritos.column(2, width=400)
    listaFavoritos.column(3, width=140)
    listaFavoritos.column(4, width=0, stretch=NO, minwidth=0)
    for f in favoritos:
        listaFavoritos.insert('', END, values=(f[0], f[1], f[2], f[3], f[4]))
    listaFavoritos.pack()
    scrollbarFavoritos.config(command = listaFavoritos.yview)
    listaFavoritos.configure(yscrollcommand=scrollbarFavoritos.set)


    ######## Ordenar lista de favoritos por columna ########
    for col in (0, 1, 2, 3, 4):
        listaFavoritos.heading(col, text=header[col], command=lambda _col=col: ordenar_lista(listaFavoritos, _col, False))


    ######## Creacion de botones de favoritos ########
    marcoBotonesFavoritos = Frame(venFavoritos)
    marcoBotonesFavoritos.pack(padx=12, pady=(10), anchor=CENTER)
    lblCosto = Label(marcoBotonesFavoritos)
    lblCosto.pack(side=RIGHT, anchor=W)
    lblSubtotal = Label(marcoBotonesFavoritos, text="Subtotal:")
    lblSubtotal.pack(padx=(200, 2), side=RIGHT, anchor=W)
    btnLink = Button(marcoBotonesFavoritos, text="Ver en la web", width=13, command=lambda: openweb(listaFavoritos.item(listaFavoritos.focus())['values'][4]))
    btnLink.pack(padx=4, side=LEFT, anchor=W)
    btnFav = Button(marcoBotonesFavoritos, text="Quitar artículo", width=16, command=lambda: borrarFavorito(listaFavoritos, listaFavoritos.item(listaFavoritos.focus())['values'][0], marcoBotonesFavoritos, lblCosto))
    btnFav.pack(padx=4, side=LEFT, anchor=W)


    ######## Creacion de subtotal ########
    
    
    actualizaSubtotal(listaFavoritos, marcoBotonesFavoritos, lblCosto)
    

def actualizaSubtotal(tv, marco, lbl):
    subtotal = StringVar()
    sumatoria = 0
    for i in tv.get_children():
        try:
            sumatoria += float(tv.item(i)["values"][3])
        except:
            continue
    subtotal.set("{0:.2f}".format(sumatoria))
    lbl["text"] = "{}".format(subtotal.get())

def agregarFavorito(producto, marco):
    if producto in favoritos:
        messagebox.showerror(title="Error", message="El producto ya se encuentra en Favoritos.")
    else:
        favoritos.append(producto)


def borrarFavorito(tv, id_producto, marco, lbl):
    for i in favoritos:
        if i[0] == id_producto:
            favoritos.remove(i)
    actualizaLista(tv)
    actualizaSubtotal(tv, marco, lbl)


def actualizaLista(tv, opc=False):
    if opc:
        productos = ArticulosBusiness().getArtsTable()
        elementos = tv.get_children()
        for e in elementos:
            tv.delete(e)
        for a, c in productos:
            tv.insert('', END, values=(a.id, c.nombre, a.nombre, a.precio, a.url))
    else:
        elementos = tv.get_children()
        for e in elementos:
            tv.delete(e)
        for i in favoritos:
            tv.insert('', END, values=(i[0], i[1], i[2], i[3], i[4]))


def ordenar_lista(tv, col, reverse):
    if col == 3 or col == 0:
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        try:
            l.sort(key=lambda t: float(t[0]), reverse=reverse)
        except:
            l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        tv.heading(col, command=lambda _col=col: ordenar_lista(tv, col, not reverse))
    else:
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        # Reordenar items.
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        # Ordenar al reves la proxima vez.
        tv.heading(col, command=lambda _col=col: ordenar_lista(tv, _col, not reverse))


def buscarProducto(opc, texto):
    articulos_seleccionados = []
    actualizaLista(lista, True)
    if opc == "Categoria":
        for i in lista.get_children():
            if texto.lower() in lista.item(i)["values"][1].lower():
                articulos_seleccionados.append(lista.item(i)["values"])
    else:
        for i in lista.get_children():
            if texto.lower() in lista.item(i)["values"][2].lower():
                articulos_seleccionados.append(lista.item(i)["values"])
    for i in lista.get_children():
        lista.delete(i)
    for i in articulos_seleccionados:
        lista.insert('', END, values=(i[0], i[1], i[2], i[3], i[4]))


def openweb(link):
    webbrowser.open(link, new=1)


######## Inicializacion ########
header = ("ID", "Categoria", "Producto", "Precio", "")
favoritos = []
articulos_existentes = []


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
desplegable.current(0)
buscador = Entry(marcoBuscador, width=50)
buscador.pack(padx=4, side=LEFT, anchor=W)
btnBuscar = Button(marcoBuscador, text="Buscar", width=6, command=lambda: buscarProducto(desplegable.get(), buscador.get()))
btnBuscar.pack(padx=10, side=RIGHT, anchor=W)


######## Creacion de la lista ########
marcoLista = Frame(root)
marcoLista.pack()
marcoLista.pack(padx=15, pady=(0, 10))
scrollbar = Scrollbar(marcoLista)
scrollbar.pack(side=RIGHT, fill=Y)
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
lista.pack()
scrollbar.config(command = lista.yview)
lista.configure(yscrollcommand=scrollbar.set)

######## Ordenar lista por columnas ########
for col in (0, 1, 2, 3, 4):
    lista.heading(col, text=header[col], command=lambda _col=col: ordenar_lista(lista, _col, False))


######## Creacion de botones ########
marcoBotones = Frame(root)
marcoBotones.pack(padx=12, pady=(10), anchor=CENTER)
btnLink = Button(marcoBotones, text="Ver en la web", width=13, command=lambda: openweb(lista.item(lista.focus())['values'][4]))
btnLink.pack(padx=4, side=LEFT, anchor=W)
btnRefresh = Button(marcoBotones, text="Actualizar", width=10, command=lambda: actualizaLista(lista, True))
btnRefresh.pack(padx=4, side=LEFT, anchor=W)
btnFav = Button(marcoBotones, text="Añadir a favoritos", width=16, command=lambda: agregarFavorito(lista.item(lista.focus())['values'], marcoBotones))
btnFav.pack(padx=4, side=LEFT, anchor=W)
actualizaLista(lista, True)

root.mainloop()
