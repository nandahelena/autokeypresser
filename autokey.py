import keyboard
import threading
import time
import tkinter as tk

is_clicking = False

def auto_key():
    global is_clicking 
    is_clicking = True

    tecla = key_entry.get()
    intervalo = float(interval_entry.get())
    duracao = float(duration_entry.get())
    ciclos = int(cycles_entry.get())

    for _ in range(ciclos):
        if not is_clicking:
            break
        start_time = time.time()
        while time.time() - start_time < duracao:
            keyboard.press(tecla)  
            time.sleep(0.05)       
        keyboard.release(tecla)  


        if intervalo > duracao:
            time.sleep(intervalo - duracao) 


def start_clicking():
    if not is_clicking:
        thread = threading.Thread(target=auto_key)
        thread.start()

def stop_clicking():
    global is_clicking
    is_clicking = False


root = tk.Tk()
root.title("Auto Key Presser")
root.geometry("300x250")

# Entrada para a tecla
tk.Label(root, text="Tecla a pressionar:").pack()
key_entry = tk.Entry(root)
key_entry.insert(0, "a") 
key_entry.pack()

# Entrada para intervalo entre cliques
tk.Label(root, text="Intervalo entre cliques (segundos):").pack()
interval_entry = tk.Entry(root)
interval_entry.insert(0, "10")  
interval_entry.pack()

# Entrada para duração da tecla pressionada
tk.Label(root, text="Duração segurando a tecla (segundos):").pack()
duration_entry = tk.Entry(root)
duration_entry.insert(0, "1")  
duration_entry.pack()

# Entrada para número de ciclos
tk.Label(root, text="Quantidade de ciclos:").pack()
cycles_entry = tk.Entry(root)
cycles_entry.insert(0, "5")  
cycles_entry.pack()

# Botões para iniciar e parar
tk.Button(root, text="Iniciar", command=start_clicking).pack()
tk.Button(root, text="Parar", command=stop_clicking).pack()

# Atalhos do teclado para iniciar e parar
keyboard.add_hotkey("F2", start_clicking)
keyboard.add_hotkey("F4", stop_clicking)

root.mainloop()