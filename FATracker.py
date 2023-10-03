import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import base64
import webbrowser
import requests
import os, sys
import json

# Icono covertido a base64
icon = """
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
"""

icon = base64.b64decode(icon)



# API configuración de Splinterlands
settings =  "https://api.splinterlands.io/settings"
player_balance = "https://api.splinterlands.io/players/balances?username="
player_details = "https://api.splinterlands.io/players/details?name="
player_renting = "https://api.splinterlands.io/market/active_rentals?renter="
player_rentout ="https://api.splinterlands.io/market/active_rentals?owner="


r = requests.get(url = settings)
data_settings = r.json()

price_sps = float(data_settings["sps_price"])
price_dec = float(data_settings["dec_price"])


# Función para guardar el nombre en una variable
def guardar_nombre():
    global account
    account = entry_nombre.get().lower()
    b = requests.get(url = player_details+account)
    data_balance = b.json()
    # Puedes imprimir el nombre para verificar que se ha guardado correctamente
    try:
        if account == data_balance["name"]:
            label_instrucciones.pack_forget()
            entry_nombre.pack_forget()
            boton_guardar.pack_forget()
            texto = f'\n\n\n\n\n\nWelcome @{data_balance["name"]}'
            etiqueta.config(text=texto, font=("Arial", 12))
    except KeyError:
        label_instrucciones.pack_forget()
        entry_nombre.pack_forget()
        boton_guardar.pack_forget()
        texto = f'\n\n\n\n\n\nThe account @{account} does not exist in Splinterlands. Try again!'
        etiqueta.config(text=texto, font=("Arial", 12))


def details():
    b = requests.get(url = player_details+account)
    data_balance = b.json()

    if data_balance["guild"] == None:
        texto = f'You joined Splinterlands on {data_balance["join_date"][0:10]}\n\nCollection Power: {data_balance["collection_power"]}\n\nWild Rating: {data_balance["rating"]}\nBattles: {data_balance["battles"]} - Wins: {data_balance["wins"]} ({round(int(data_balance["wins"])*100/int(data_balance["battles"]),2)}%)\n\nModern Rating: {data_balance["modern_rating"]}\nBattles: {data_balance["modern_battles"]} - Wins: {data_balance["modern_wins"]} ({round(int(data_balance["modern_wins"])*100/int(data_balance["modern_battles"]),2)}%)\n\n\nThe Fallen Angels guild is looking for members like you.\nMore information at https://fallenangels.pythonanywhere.com/'
        messagebox.showinfo("", "Don't belong to a guild? Join Fallen Angels.")
        # Crear una función que se llame al hacer clic en el enlace
        def abrir_enlace(event):
            webbrowser.open_new("https://fallenangels.pythonanywhere.com/")
        etiqueta.config(text=texto, font=("Arial", 12))
        etiqueta.bind("<Button-1>", abrir_enlace)  # Vincula la función al hacer clic
    else:
        texto = f'You joined Splinterlands on {data_balance["join_date"][0:10]}\n\nCollection Power: {data_balance["collection_power"]}\n\nWild Rating: {data_balance["rating"]}\nBattles: {data_balance["battles"]} - Wins: {data_balance["wins"]} ({round(int(data_balance["wins"])*100/int(data_balance["battles"]),2)}%)\n\nModern Rating: {data_balance["modern_rating"]}\nBattles: {data_balance["modern_battles"]} - Wins: {data_balance["modern_wins"]} ({round(int(data_balance["modern_wins"])*100/int(data_balance["modern_battles"]),2)}%)\n\n\n⚔⚔⚔ You are a member of the {data_balance["guild"]["name"]} guild ⚔⚔⚔'
        etiqueta.config(text=texto, font=("Arial", 12))



def sps():
    b = requests.get(url = player_balance+account)
    data_balance = b.json()

    for i in data_balance:
        if i["token"] == "SPS":
            sps = float(i["balance"])
        elif i["token"] == "SPSP":
            spsp = float(i["balance"])
    resumen = f"SPS and Staked SPS of the account @{account} is:\n\n\n"
    texto = f"SPS: {round(sps,2)} (${round(sps*price_sps,2)})\nStaked SPS: {round(spsp,2)} (${round(spsp*price_sps,2)})\nTOTAL: {round(sps+spsp,2)} (${round((sps+spsp)*price_sps,2)})"

    etiqueta.config(text=resumen+texto, font=("Arial", 12))


def dec():
    b = requests.get(url = player_balance+account)
    data_balance = b.json()

    for i in data_balance:
        if i["token"] == "DEC":
            dec = float(i["balance"])

    resumen = f"DEC of the account @{account} is:\n\n\n"
    texto = f"DEC: {round(dec,2)} (${round(dec*price_dec,2)})"

    etiqueta.config(text=resumen+texto, font=("Arial", 12))


def gastos_alquiler():
    rt = requests.get(url = player_renting+account)
    data_trades = rt.json()
    rent = 0

    for data in data_trades:
        rent += float(data["buy_price"])

    resumen = f"Summary of daily rental costs of the @{account} account:\n\n\n"
    texto = f"Rental costs: {round(rent,2)} DEC/diary - ${round(rent*price_dec,2)}/diary"

    etiqueta.config(text=resumen+texto, font=("Arial", 12))


def ingresos_alquiler():
    rt = requests.get(url = player_rentout+account)
    data_trades = rt.json()
    rentout = 0

    for data in data_trades:
        rentout += float(data["buy_price"])

    resumen = f"Summary of daily rental income in the @{account} account:\n\n\n"
    texto = f"Rental income: {round(rentout,2)} DEC/diary - ${round(rentout*price_dec,2)}/diary"

    etiqueta.config(text=resumen+texto, font=("Arial", 12))



def salir():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        ventana.quit()

# Función para mostrar un mensaje de acerca de
def acerca_de():
    messagebox.showinfo("About FATracker", "FATracker is a program to instantly know the data of your Splinterlands accounts.\n\nDeveloped by @javivisan for Fallen Angels guild.")


ventana = tk.Tk()
ventana.title("FATracker v0.1.1 by Fallen Angels Guild")

# Establecer el tamaño de la ventana
ventana.geometry("600x400")  # Ancho x Alto


# Etiqueta para instrucciones
label_instrucciones = tk.Label(ventana, text="\n\n\nPlease, enter your username:")
label_instrucciones.pack()

# Campo de entrada de texto
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# Botón para guardar el nombre
boton_guardar = tk.Button(ventana, text="Select", command=guardar_nombre)
boton_guardar.pack()

# Establecer el icono
#ventana.iconbitmap("favicon.ico")  # Reemplaza "icono.ico" con la ruta de tu propio archivo de icono
icon = PhotoImage(data=icon)
ventana.wm_iconphoto(True, icon)

# Crear la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=False)
barra_menu.add_cascade(label="File", menu=menu_archivo)

menu_archivo.add_command(label="Exit", command=salir)

# Menú Cuenta
menu_cuenta = tk.Menu(barra_menu, tearoff=False)
barra_menu.add_cascade(label="My Account", menu=menu_cuenta)

menu_cuenta.add_command(label="Details", command=details)
menu_cuenta.add_command(label="DEC", command=dec)
menu_cuenta.add_command(label="SPS", command=sps)
menu_cuenta.add_separator()  # Agregar un separador
menu_cuenta.add_command(label="Rental Costs", command=gastos_alquiler)
menu_cuenta.add_command(label="Rental Income", command=ingresos_alquiler)


# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=False)
barra_menu.add_cascade(label="Help", menu=menu_ayuda)

menu_ayuda.add_command(label="About FATracker", command=acerca_de)


# Etiqueta para mostrar el texto
etiqueta = tk.Label(ventana, text="", padx=20, pady=20)
etiqueta.pack()


ventana.mainloop()
