import threading
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import sys

alarma_hora = None

#Actualizar la hora
def actualizar_reloj():
    while True:
        ahora = datetime.now()
        hora_actual = ahora.strftime("%I:%M:%S %p")  # Formato AM/PM
        etiqueta_hora.config(text=hora_actual)

        #Verifica si la hora es igual a la alarma
        if alarma_hora and ahora.strftime("%I:%M:%S %p") == alarma_hora:
            messagebox.showinfo("Alarma", "¡Es hora!")      
        time.sleep(1)

#Establecer la alarma
def establecer_alarma():
    global alarma_hora
    hora_alarma = entrada_alarma.get()

    try:
        #Convierte a formato de 12 horas
        datetime.strptime(hora_alarma, "%I:%M:%S %p")
        alarma_hora = hora_alarma
        etiqueta_alarma.config(text=f"Alarma establecida a: {alarma_hora}")
    except ValueError:
        messagebox.showerror("Error", "Formato inválido. Usa HH:MM:SS AM/PM")

#Crea ventana
ventana = tk.Tk()
ventana.title("Alarma")
ventana.geometry("350x250")

#Mostrar hora actual
etiqueta_hora = tk.Label(ventana, font=("Arial", 30))
etiqueta_hora.pack(pady=20)

#Entrada alarma
entrada_alarma = tk.Entry(ventana, font=("Arial", 14))
entrada_alarma.pack()
entrada_alarma.insert(0, "12:00:00 AM")  #Ejemplo 

#Botón para establecer alarma
boton_alarma = tk.Button(ventana, text="Establecer Alarma", command=establecer_alarma)
boton_alarma.pack(pady=5)

#Mostrar hora de la alarma establecida
etiqueta_alarma = tk.Label(ventana, text="Sin alarma", font=("Arial", 12))
etiqueta_alarma.pack()

# Iniciar hilo para actualizar la hora
hilo_reloj = threading.Thread(target=actualizar_reloj, daemon=True)
hilo_reloj.start()

# Ejecutar
ventana.mainloop()
