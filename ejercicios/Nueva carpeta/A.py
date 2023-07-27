import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se debera cargar el peso* de un articulo, el cual podra ser ingresado en gramos o en onzas 

    La unidad de medida es indicada mediante una lista desplegable.

* Flotantes mayores que cero

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los pesos en gramos, en onzas y su posicion en la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al precionar el boton Informar 
    0- Valor (en onzas) y posicion del articulo mas pesado
    1- Valor (en gramos) y posicion del articulo mas liviano
     2- Peso promedio (en onzas) 
     3- Peso promedio (en gramos)
    4- Informar los pesos que superan el promedio (en gramos)
    5- Informar los pesos que NO superan el promedio (en onzas)
    6- Informar la cantidad de articulos que superan el peso promedio
    7- Informar la cantidad de articulos que NO superan el peso promedio
    8- Indicar los pesos repetidos (gramos)
    9- Indicar los pesos NO repetidos (gramos)


1 gramo son 0.035274 oz
1 oz son 28.3495 gramos
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RECUPERATORIO EXAMEN INGRESO")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="PESO")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_tipo_de_peso = customtkinter.CTkComboBox(master=self, values=["Gramos","Onzas"])
        self.combobox_tipo_de_peso.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_pesos = []


    def btn_agregar_on_click(self):
        peso = self.txt_peso_articulo.get()
        unidad = self.combobox_tipo_de_peso.get()
        peso_valido = False
        contador_punto = 0

        for letra in peso:
            if not letra.isdigit() and letra != ".":
                peso_valido = False
            elif letra == ".":
                contador_punto += 1
                if contador_punto > 1:
                    peso_valido = False
            elif peso == "0":
                peso_valido = False
            elif float(peso) <= 0:
                peso_valido =False
            else:
                peso_valido = True


        if peso_valido:
            alert ("Datos","El peso se ingreso correctamente")
        else:
            alert ("Datos","El peso no es valido")

        self.txt_peso_articulo.delete(0,100)

        peso = float(peso)
 
        if unidad == "Onzas":
            peso = peso * 28.3495

        self.lista_pesos.append(peso)

    def btn_mostrar_on_click(self):

        lista_pesos = ""
        for peso in self.lista_pesos:
            lista_pesos += str(peso) + " grs\n" 
        alert("lista",f"{lista_pesos}")

        lista_pesos_oz = []
        for peso in self.lista_pesos:
            peso = peso / 28.3495
            lista_pesos_oz.append(peso)

        lista_pesos_oz_txt = ""
        for peso in lista_pesos_oz:
            lista_pesos_oz_txt += str(peso) + " oz\n" 

        alert ("Lista",f"{lista_pesos_oz_txt}")

        
        
    def btn_informar_on_click(self):
        promedio_g = 0
        promedio_oz = 0
        peso_total_g = 0
        peso_total_oz = 0
        contador = 0

        for suma in self.lista_pesos:
            peso_total_g += suma
            contador += 1

        promedio_g = peso_total_g / contador

        for suma in self.lista_pesos:
            suma = suma * 28.3495 
            peso_total_oz += suma

        promedio_oz = peso_total_oz / contador

        alert("Pesos","El peso promedio en gramos es de: "+str(promedio_g)+"grs"+"\nEl peso promedio en onzas es de: "+str(promedio_oz)+"oz")

        pesos_altos_g = []
        pesos_altos_g_txt = ""
        pesos_altos_oz = []
        pesos_altos_oz_txt = ""

        for suma in self.lista_pesos:
            if suma > promedio_g:
                pesos_altos_g.append(suma)
                
        for suma in pesos_altos_g:
            pesos_altos_g_txt = str(suma) + "grs\n"
        
        alert ("Lista",f"Los pesos por encima del promedio en gramos son: {pesos_altos_g_txt}")

        for suma in self.lista_pesos:
            suma = suma * 28.3495
            if suma < promedio_oz:
                pesos_altos_oz.append(suma)

        for suma in pesos_altos_oz:
            pesos_altos_oz_txt = str(suma) + "oz\n"
        alert ("Lista",f"Los pesos por debajo del promedio en onzas son: {pesos_altos_oz_txt}")
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
