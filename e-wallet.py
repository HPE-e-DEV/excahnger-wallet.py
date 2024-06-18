from tkinter import *
from tkinter import ttk
import requests

#Definir ventana
ventana = Tk() 
ventana.minsize(500, 500)
ventana.title("Exchange realizado en Python |For HPE e-wallet")
ventana.resizable(0,0)

#Método para convertir de una moneda a otra
def conversion():
    try:
        url = 'https://v6.exchangerate-api.com/v6/TU-API-KEY/latest/'+moneda1.get()
        response = requests.get(url)
        data = response.json()
        resultado = round((float(numero_entry.get()) * data['conversion_rates'][moneda2.get()]), 2)
        espacio = Label(ventana, text="")
        espacio.grid(row=7, column=0)
        resultado_label = Label(ventana, text=resultado)
        resultado_label.grid(row=8, column=0)
        resultado_label.config(
            fg="black",
            bg="white",
            font=("Arial", 20),
            padx=400,
            pady=20
        )
    except:
        espacio = Label(ventana, text="")
        espacio.grid(row=7, column=0)
        resultado_label = Label(ventana, text="Hay algo incorrecto. Recuerda que solo puedes escribir NÚMEROS")
        resultado_label.grid(row=8, column=0)
        resultado_label.config(
            fg="red",
            bg="black",
            font=("Arial", 20),
            padx=100,
            pady=20
        )
        
#Diseño del título
home_label = Label(ventana, text="¡Exchange de todas las monedas!")
home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
home_label.grid(row=0, column=0)

#Diseño del número y moneda 1
numero_label = Label(ventana, text="Dime el número y la moneda correspondiente")
numero_entry = Entry(ventana)
numero_label.grid(row=1, column=0, padx=5, pady=5)
numero_entry.grid(row=2, column=0, padx=5, pady=5)
moneda1 = ttk.Combobox()
moneda1 = ttk.Combobox(state="readonly")
moneda1["values"] = ["USD", 'Bsd','AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'DOP', 'EGP', 'EUR', 'FJD', 'GBP', 'GTQ', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'KZT', 'MVR', 'MXN', 'MYR', 'NOK', 'NZD', 'PAB', 'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'RON', 'RUB', 'SAR', 'SEK', 'SGD', 'THB' 'TRY', 'TWD', 'UAH', 'UYU', 'ZAR']
moneda1.grid(row=3, column=0, padx=5, pady=5)

#Diseño de moneda 2
moneda2_label = Label(ventana, text="A qué moneda lo quieres convertir?")
moneda2_label.grid(row=4, column=0, padx=5, pady=5)
moneda2 = ttk.Combobox()
moneda2 = ttk.Combobox(state="readonly")
moneda2["values"] = ["USD", 'AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'DOP', 'EGP', 'EUR', 'FJD', 'GBP', 'GTQ', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'KZT', 'MVR', 'MXN', 'MYR', 'NOK', 'NZD', 'PAB', 'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'RON', 'RUB', 'SAR', 'SEK', 'SGD', 'THB' 'TRY', 'TWD', 'UAH', 'UYU', 'ZAR']
moneda2.grid(row=5, column=0, padx=5, pady=5)

#Botón para hacer funcionar el método
boton = Button(ventana, text="Convertir", command=conversion)
boton.grid(row=6, column=0)

ventana.mainloop()
