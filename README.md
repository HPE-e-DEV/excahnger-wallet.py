Bueno, imagino que antes de programar una cosa, querrás saber qué es dicha cosa. Para ello, te comento lo que dice Wikipedia sobre ello:

Los exchanges, también conocidos como plataformas o mercados de intercambio, son plataformas digitales que permiten intercambiarmonedas digitales por dinero fiat y/u otras criptomonedas o mercancías.

Es una explicación rara a la par de explícita única y exclusivamente enfocada a las criptomonedas.

Pero, en realidad, un exchange se define cómo un sitio, web o (en nuestro caso) programa para introducir un valor en una determinada moneda o criptomoneda.

Y eso es lo que vamos a hacer nosotros hoy, vamos a crear una interfaz gráfica, o GUI por sus siglas en inglés en el cual, el usuario insertará un valor en una determinada moneda y el programa mostrará su valor actual a tiempo real.

ANTES DE COMENZAR NECESITAS SABER QUE:

Una API (palabra que verás dentro de unos instantes) es (según la definición de la web de Red Hat) un conjunto de definiciones y protocolos que se utilizan para desarrollar e integrar el software de las aplicaciones. API significa interfaz de programación de aplicaciones.

En resumen, una API suele ser un archivo de un programa independiente, programado única y exclusivamente para ser integrado en otras aplicaciones.

Oye, ¿cómo haremos para que se muestre el valor actual, si esto es un mercado que varía a cada segundo?

Voy a proceder a explicarte todo, paso a paso, tal y cómo hacemos siempre aquí. Pero antes, te voy a enseñar un pequeño GIF de lo que vas a aprender a programar leyendo este simple post! 😁


Ahora sí que sí, aquí llega el primer paso 1️⃣.

Debemos registrarnos en ExchanGerate-API, que es una API libre, abierta y gratuita para realizar conversiones entre monedas de las más variopintas.

El registro es sencillo, simplemente deberemos escribir el correo electrónico al que queramos que llegue la clave gratuita y darle al botón.


Una vez que nos registremos, en nuestro dashboard aparecerá un número muy largo. Dicho número es la clave del API que posteriormente vamos a usar en Python 🐍.

Cuando tengamos dicho código. Vamos a empezar por abrir nuestro IDE favorito. Que en mi caso es VSCode y empezaremos a importar los paquetes que vamos a necesitar en este proyecto. 📦

Aunque lo digo siempre que hago un post sobre Python, recuerdo que en este lenguaje de programación no es necesario precisar de qué tipo será la variable (Char, float, entero,…), a diferencia de otros muchos lenguajes de programación ya que, Python 🐍, entenderá automáticamente el tipo de variable según lo que guardemos en él.

Para este proyecto vamos a importar tkinter de las siguientes formas from tkinter import * y from tkinter import ttk. Estos dos, serán obviamente, para realizar la interfaz gráfica del programa.
Por último, debemos importar también el paquete de requests, que trabaja con páginas webs para decodificar su JSON, extraer información y muchísimo más. El código es import requests.

MUCHO OJO 👀, probablemente os dé fallo con el paquete requests, y esto es porque hay que instalarlo primeramente en la línea de comandos usando el instalador pip. pip install requests

Recordatorio 🧠
Los comentarios en Python se escriben poniendo al comienzo de la línea el símbolo #
Las funciones en la programación. Las funciones, de manera resumida, es un trozo de código que, aunque esté escrita, nunca se accionará hasta que sea invocada. 🧙🏻‍♂️

TKinter 🎨
Tenemos que crear una ventana raíz estableciendo un nombre antes de Tk().
Posteriormente le damos el tamaño de la ventana con minsize(valorx, valory).
Establecemos un título para la ventana con title(“Nombre”)
Y para que ningún usuario pueda ampliar o reducir el tamaño de la ventana, estableceremos a 0 los dos parámetros de resizable(x,y).

Añadiendo todo esto, nuestro programa comienza así:

Python
1
from tkinter import *
2
from tkinter import ttk
3
import requests
4
​
5
#Definición ventana
6
ventana = Tk() 
7
ventana.minsize(500, 500)
8
ventana.title("Exchange realizado en Python | fcoterroba.com")
9
ventana.resizable(0,0)
Vamos a hacer ahora lo tocho, todo lo que aparecerá en nuestra ventana principal.

1️⃣ Primeramente, vamos a escribir un Label a modo de título del programa, dándole su respectiva configuración de diseño y distribución.

Python
1
titulo_label = Label(ventana, text="¡Exchange de todas las monedas!")
2
titulo_label.config(
3
        fg="white",
4
        bg="black",
5
        font=("Arial", 30),
6
        padx=210,
7
        pady=20
8
    )
9
titulo_label.grid(row=0, column=0)
2️⃣ Lo segundo, establecer la entrada de texto, aunque sea un número, Tkinter no hace distinción de ello, por lo que seremos nosotros quienes daremos una alerta si no es un número.
La entrada de texto se almacenará en una variable que debemos declarar previamente. Yo lo he hecho justo en la línea de debajo de ventana.resizable

Python
1
numero_label = Label(ventana, text="Dime el número y la moneda correspondiente")
2
numero_entry = Entry(ventana, textvariable=numero_data)
3
numero_label.grid(row=1, column=0, padx=5, pady=5)
4
numero_entry.grid(row=2, column=0, padx=5, pady=5)
3️⃣ La tercera parte es crear los Combobox. Estos elementos son como unas listas desplegables vistos en el desarrollo web u otros.
Para crearlas en Python debes darle un nombre seguido de ttk.Combobox().
Luego, has de bloquear que el usuario pueda escribir encima de la lista con ttk.Combobox(state=”readonly”)
Por último, debes escribir todos los valores que quieres que aparezcan en dicho Combobox. En este caso, serán todas las monedas disponibles en la API.
Esto hay que repetirlo dos veces, primero para la moneda de tu dinero y luego la moneda a la que quieras convertirla.

Python
1
combo = ttk.Combobox()
2
combo = ttk.Combobox(state="readonly")
3
combo["values"] = ["USD", 'AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'DOP', 'EGP', 'EUR', 'FJD', 'GBP', 'GTQ', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'KZT', 'MVR', 'MXN', 'MYR', 'NOK', 'NZD', 'PAB', 'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'RON', 'RUB', 'SAR', 'SEK', 'SGD', 'THB' 'TRY', 'TWD', 'UAH', 'UYU', 'ZAR']
4
combo.grid(row=3, column=0, padx=5, pady=5)
5
second_moneda = Label(ventana, text="A qué moneda lo quieres convertir?")
6
second_moneda.grid(row=4, column=0, padx=5, pady=5)
7
combo2 = ttk.Combobox()
8
combo2 = ttk.Combobox(state="readonly")
9
combo2["values"] = ["USD", 'AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'DOP', 'EGP', 'EUR', 'FJD', 'GBP', 'GTQ', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'KZT', 'MVR', 'MXN', 'MYR', 'NOK', 'NZD', 'PAB', 'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'RON', 'RUB', 'SAR', 'SEK', 'SGD', 'THB' 'TRY', 'TWD', 'UAH', 'UYU', 'ZAR']
10
combo2.grid(row=5, column=0, padx=5, pady=5)
4️⃣ Seguimos con el cuarto paso, que es realizar el botón con el comando de una función que haremos en el siguiente paso. Función que realizará toda la lógica de la conversión y mostrará el resultado.
También, que no se nos olvide ❗ nuestro preciado mainloop. Para que el programa aparezca visualmente.

Python
1
boton = Button(ventana, text="Convertir", command=conversion)
2
boton.grid(row=6, column=0)
3
ventana.mainloop()
5️⃣ En nuestro quinto paso vamos a crear una función con el nombre que le hemos dado a la propiedad command de nuestro botón. def conversion():
Dentro de dicha función, vamos a hacer un try/except principalmente para cuando el usuario inserte algo distinto de números.
TRY
Vamos a crear una variable para obtener la URL de la API añadiendole al final la moneda número 1 con combo.get().
A continuación, creamos una variable response para que obtenga los requests de la url con requests.get(url).
Después, creamos otra variable data para almacenar el json de response.

Y ahora sí, empezamos con las mates! 🔣
Hemos de pasar el número que tenemos a float, creando una nueva variable.
Para finalizar debemos crear una nueva variable resultado multiplicando dicho número float por la moneda existente en el archivo JSON.

Dicho esto, solo nos faltaría establecer un diseño y voilá.

EXCEPT
Simplemente vamos a copiar el diseño hecho para el resultado anterior, poniendo un texto sobre la errata y hacerlo algo más llamativo.

Python
1
def conversion():
2
    try:
3
        url = 'https://v6.exchangerate-api.com/v6/TU-API-KEY/latest/'+combo.get()
4
        response = requests.get(url)
5
        data = response.json()
6
        numero1 = float(numero_entry.get())
7
        resultado = round((numero1 * data['conversion_rates'][combo2.get()]), 2)
8
        espacio = Label(ventana, text="")
9
        espacio.grid(row=7, column=0)
10
        resultado_label = Label(ventana, text=resultado)
11
        resultado_label.grid(row=8, column=0)
12
        resultado_label.config(
13
            fg="black",
14
            bg="white",
15
            font=("Arial", 20),
16
            padx=400,
17
            pady=20
18
        )
19
    except:
20
        espacio = Label(ventana, text="")
21
        espacio.grid(row=7, column=0)
22
        resultado_label = Label(ventana, text="Hay algo incorrecto. Recuerda que solo puedes escribir NÚMEROS")
23
        resultado_label.grid(row=8, column=0)
24
        resultado_label.config(
25
            fg="red",
26
            bg="black",
27
            font=("Arial", 20),
28
            padx=100,
29
            pady=20
30
        )
Si no nos hemos saltado ningún paso, nuestro proyecto debería quedar algo más o menos así:

from tkinter import *
from tkinter import ttk
import requests

#Definir ventana
ventana = Tk() 
ventana.minsize(500, 500)
ventana.title("Exchange realizado en Python | fcoterroba.com")
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
moneda1["values"] = ["USD", 'AED', 'ARS', 'AUD', 'BGN', 'BRL', 'BSD', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'DOP', 'EGP', 'EUR', 'FJD', 'GBP', 'GTQ', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'KZT', 'MVR', 'MXN', 'MYR', 'NOK', 'NZD', 'PAB', 'PEN', 'PHP', 'PKR', 'PLN', 'PYG', 'RON', 'RUB', 'SAR', 'SEK', 'SGD', 'THB' 'TRY', 'TWD', 'UAH', 'UYU', 'ZAR']
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
