
from tkinter import tk, Text

class Interfaz:
    def __init__(self, ventana):
       
        self.ventana=ventana
        self.ventana.title("Calculadora")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana, state="disabled", width=40, height=3, background="orchid", foreground="white", font=("Helvetica",15))

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""

        return


ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()