import tkinter as tk
import os

def shutdown(seconds):
    os.system(f"shutdown /s /t {seconds}")

def shutdown_10_seconds():
    shutdown(10)

def shutdown_20_minutes():
    shutdown(20 * 60)

def shutdown_40_minutes():
    shutdown(40 * 60)

def shutdown_1_hour():
    shutdown(60 * 60)

def shutdown_custom():
    try:
        seconds = int(entry.get())
        shutdown(seconds)
    except ValueError:
        label.config(text="Por favor, introduce un número válido en segundos", fg="red")

# -- Ventana principal
root = tk.Tk()
root.title("Scheduled Shutdown")
root.geometry("350x270")
root.configure(bg="#282c34")

button_style = {"font": ("Arial", 12, "bold"), "width": 20, "height": 1, "bg": "#61afef", "fg": "white", "bd": 0}
label_style = {"font": ("Arial", 12), "bg": "#282c34", "fg": "white"}
entry_style = {"font": ("Arial", 12), "bd": 2, "relief": "flat"}

# -- Botones
button_10_seconds = tk.Button(root, text="10 segundos", command=shutdown_10_seconds, **button_style)
button_10_seconds.pack(pady=5)

button_20_minutes = tk.Button(root, text="20 minutos", command=shutdown_20_minutes, **button_style)
button_20_minutes.pack(pady=5)

button_40_minutes = tk.Button(root, text="40 minutos", command=shutdown_40_minutes, **button_style)
button_40_minutes.pack(pady=5)

button_1_hour = tk.Button(root, text="1 hora", command=shutdown_1_hour, **button_style)
button_1_hour.pack(pady=5)

entry_label = tk.Label(root, text="Introduce el tiempo en segundos:", **label_style)
entry_label.pack(pady=5)

entry = tk.Entry(root, **entry_style)
entry.pack(pady=5)

button_custom = tk.Button(root, text="Programar apagado", command=shutdown_custom, **button_style)
button_custom.pack(pady=5)

label = tk.Label(root, text="", **label_style)
label.pack(pady=5)

# -- Ejecución
root.mainloop()
