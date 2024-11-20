from tkinter import *
import math
import sympy as sp
import pandas as pd

# Características básicas
raiz = Tk()
raiz.title("Calculadora WmU Extrapolación Richardson")
raiz.resizable(False,False)
raiz.geometry("500x550")

# Frame para decorar
frame = Frame(raiz, bg="black",width=490, height=540) 
frame.place(relx=0.5, rely=0.5, anchor='center')

# Centrar 
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()

ancho_ventana = 500
alto_ventana = 550

x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
y_pos = (alto_pantalla // 2) - (alto_ventana // 2)
raiz.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

# Título
titulo = Label(raiz,text="Método Extrapolación de Richardson", font=("Impact",20), fg="thistle", bg="black")
titulo.pack(pady=20)

# Entradas
funcion = Label(raiz, text="Ingrese la función: ", font=("Times New Roman",12), fg="white", bg="black")
funcion.pack(pady=10)

eFuncion = Entry(raiz,width=40, highlightbackground="lightgreen")
eFuncion.pack(pady=5)

valorX = Label(raiz, text="Ingrese el punto en el que se va a evaluar: ", font=("Times New Roman",12), fg="white", bg="black")
valorX.pack(pady=10)

eValorX = Entry(raiz,width=40, highlightbackground="lightgreen")
eValorX.pack(pady=5)

valorP = Label(raiz, text="Ingrese el valor de p: ", font=("Times New Roman",12), fg="white", bg="black")
valorP.pack(pady=10)

eValorP = Entry(raiz,width=40, highlightbackground="lightgreen")
eValorP.pack(pady=5)

valorH = Label(raiz, text="Ingrese el valor de h: ", font=("Times New Roman",12), fg="white", bg="black")
valorH.pack(pady=10)

eValorH = Entry(raiz,width=40, highlightbackground="lightgreen")
eValorH.pack(pady=5)

valorQ = Label(raiz, text="Ingrese el valor de q: ", font=("Times New Roman",12), fg="white", bg="black")
valorQ.pack(pady=10)

eValorQ = Entry(raiz,width=40, highlightbackground="lightgreen")
eValorQ.pack(pady=5)

# Etiqueta para mostrar resultados en la ventana principal
label_resultado = Label(raiz, bg="black", fg="white")
label_resultado.pack(pady=5)

# Cálculos
def calcular():
    try:
        pd.options.display.float_format = '{:.10f}'.format

        funcion_usuario = eFuncion.get()
        X = float(eValorX.get())
        p = float(eValorP.get())
        h = float(eValorH.get())
        q = float(eValorQ.get())

        # Usar sympy para convertir la función en una función que acepte un valor numérico
        x = sp.symbols('x')
        f_sym = eval(funcion_usuario.replace('math.', 'sp.'))
        f = sp.lambdify(x, f_sym, 'math')
        
        # Calculamos f(h) y f(h/q)
        Fh = (f(X + h) - f(X)) / h
        Fhq = (f(X + (h / q)) - f(X)) / (h / q)
        
        resultado = Fh + ((Fh - Fhq) / (q**(-p) - 1))
        
        respuesta = f"El valor de la derivada es: \n{resultado:.10f}"
            
        # Crear ventana de respuesta
        ventana_resultado = Toplevel(raiz)
        ventana_resultado.title("Resultado")
        ventana_resultado.geometry("400x230")
        ventana_resultado.resizable(False,False)
        
        # Centrar
        ancho_ventana_resultado = 400
        alto_ventana_resultado = 230

        x2_pos = (ancho_pantalla // 2) - (ancho_ventana_resultado // 2)
        y2_pos = (alto_pantalla // 2) - (alto_ventana_resultado // 2)
        ventana_resultado.geometry(f"{ancho_ventana_resultado}x{alto_ventana_resultado}+{x2_pos}+{y2_pos}")
        
        frame2 = Frame(ventana_resultado, bg="black", width=390, height=220) 
        frame2.place(relx=0.5, rely=0.5, anchor='center')
        
        resp = Label(ventana_resultado, text="Resultado", font=("Times New Roman", 16, "bold"), bg="black", fg="thistle")
        resp.pack(pady=20)
        
        # Mostrar el resultado
        label_resultado_ventana = Label(ventana_resultado, text=respuesta, font=("Times New Roman", 14), bg="black", fg="white", justify="left")
        label_resultado_ventana.pack(pady=8)

        # Botón para cerrar la nueva ventana
        boton_cerrar = Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, fg="black", bg="thistle")
        boton_cerrar.pack(pady=10)
            
    except ValueError:
        label_resultado.config(text="Por favor, ingresa números válidos.")
    except Exception as e:
        label_resultado.config(text=f"Error: {str(e)}")

boton = Button(raiz, text="Calcular", command=calcular, bg="thistle")
boton.pack(pady=25)

raiz.mainloop()