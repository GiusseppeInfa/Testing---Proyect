import tkinter as tk
from tkinter import messagebox

usuarios = {
    "profe1": "1234",
    "admin": "admin"
}

estudiantes = {
    "1": {"nombre": "Leonardo Leonesco", "notas": []},
    "2": {"nombre": "Adrian SantaCruz", "notas": []}
}

# -------- FUNCIONES --------

def validar_login():
    user = entry_user.get()
    password = entry_pass.get()

    if user in usuarios and usuarios[user] == password:
        ventana_login.destroy()
        abrir_menu()
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")


def registrar_nota():
    codigo = entry_codigo.get()

    if codigo not in estudiantes:
        messagebox.showerror("Error", "Estudiante no existe")
        return

    try:
        nota = float(entry_nota.get())

        if nota < 0 or nota > 20:
            messagebox.showerror("Error", "Nota fuera de rango")
            return

        estudiantes[codigo]["notas"].append(nota)
        messagebox.showinfo("Éxito", "Nota registrada")

    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")


def calcular_promedio(codigo):
    notas = estudiantes[codigo]["notas"]
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def mostrar_historial():
    codigo = entry_codigo.get()

    if codigo not in estudiantes:
        messagebox.showerror("Error", "Estudiante no existe")
        return

    estudiante = estudiantes[codigo]
    promedio = calcular_promedio(codigo)

    texto = f"Nombre: {estudiante['nombre']}\n"
    texto += f"Notas: {estudiante['notas']}\n"
    texto += f"Promedio: {promedio:.2f}\n"
    texto += "Estado: Aprobado" if promedio >= 11 else "Estado: Desaprobado"

    messagebox.showinfo("Historial", texto)


# -------- VENTANAS --------

def abrir_menu():
    global entry_codigo, entry_nota

    ventana = tk.Tk()
    ventana.title("Sistema de Notas")

    tk.Label(ventana, text="Código estudiante").pack()
    entry_codigo = tk.Entry(ventana)
    entry_codigo.pack()

    tk.Label(ventana, text="Nota").pack()
    entry_nota = tk.Entry(ventana)
    entry_nota.pack()

    tk.Button(ventana, text="Registrar Nota", command=registrar_nota).pack(pady=5)
    tk.Button(ventana, text="Mostrar Historial", command=mostrar_historial).pack(pady=5)

    ventana.mainloop()


# -------- LOGIN --------

ventana_login = tk.Tk()
ventana_login.title("Login")

tk.Label(ventana_login, text="Usuario").pack()
entry_user = tk.Entry(ventana_login)
entry_user.pack()

tk.Label(ventana_login, text="Contraseña").pack()
entry_pass = tk.Entry(ventana_login, show="*")
entry_pass.pack()

tk.Button(ventana_login, text="Ingresar", command=validar_login).pack(pady=10)

ventana_login.mainloop()