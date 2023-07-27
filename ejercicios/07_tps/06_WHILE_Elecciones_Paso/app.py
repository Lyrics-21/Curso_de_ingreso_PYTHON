'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
      cantidad_votos_maxima = False
      edad_votos_minimo = 0
      suma_edad = 0
      total_candidatos = 0
      votos_totales = 0
      nombre_votos_maximo = ""
      nombre_votos_minimo = ""


      while True:
       
        nombre = prompt("Info", "Ingrese el nombre del candidato")
        while not nombre.isalpha():
            nombre = prompt("Error", "Ingrese el nombre del candidato de nuevo")

        edad = prompt("Info", "ingrese la edad del candidato")
        while not edad.isdigit() or int(edad) <25 or int(edad) >90:
            edad = prompt("Error", "ingrese de nuevo la edad del candidato")

        votos = prompt("Info","Ingrese la cantidad de votos")
        while not votos.isdigit() or int(votos) < 0:
            votos = prompt("Error", "ingrese de nuevo los votos")

        votos = int(votos)
        edad = int(edad)

        suma_edad = edad + suma_edad
        total_candidatos +=1
        votos_totales = votos + votos_totales

        if cantidad_votos_maxima == False:
            cantidad_votos_maxima = True
            nombre_votos_maximo = nombre
            nombre_votos_minimo = nombre

        if votos > cantidad_votos_maxima:
            cantidad_votos_maxima = votos
            nombre_votos_maximo = nombre
        elif votos < cantidad_votos_maxima:

            nombre_votos_minimo = nombre 
            edad_votos_minimo = edad

        promedio = suma_edad / total_candidatos
            
        continuar = question("","Desea continuar")
        if continuar == False: 
          break

      alert("Listo","El candidato con mas votos es: "+nombre_votos_maximo+"\nEl candidato con menos votos es: "+nombre_votos_minimo+" Y tiene "+str(edad_votos_minimo)+" Años"+"\nEl promedio de las edades es de: "+str(promedio)+" años"+"\nEl total de votos emitidos es de: "+str(cantidad_votos_maxima)+" votos")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
