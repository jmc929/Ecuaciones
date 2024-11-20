from tkinter import *
import math
import sympy as sp
import pandas as pd

#Características básicas
raiz = Tk()
raiz.title("Calculadora WmU Trapecio Compuesto")
raiz.resizable(False,False)
raiz.geometry("500x500")

#Frame para decorar
frame = Frame(raiz, bg="black",width=490, height=490) 
frame.place(relx=0.5, rely=0.5, anchor='center')

#centrar 
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()

ancho_ventana = 500
alto_ventana = 500

x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
y_pos = (alto_pantalla // 2) - (alto_ventana // 2)
raiz.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

#Titulo
titulo = Label(raiz,text="Método del Trapecio Compuesto", font=("Impact",20), fg="lightblue", bg="black")
titulo.pack(pady=20)

#Entradas
funcion = Label(raiz, text="Ingrese la función: ", font=("Times New Roman",12), fg="white", bg="black")
funcion.pack(pady=10)

eFuncion = Entry(raiz,width=40, highlightbackground="lightgreen")
eFuncion.pack(pady=5)

valorLI = Label(raiz, text="Ingrese el límite inferior: ", font=("Times New Roman",12), fg="white", bg="black")
valorLI.pack(pady=10)

eValorLI = Entry(raiz,width=40, highlightbackground="lightgreen")
eValorLI.pack(pady=5)

valorLS = Label(raiz, text="Ingrese el límite superior: ", font=("Times New Roman",12), fg="white", bg="black")
valorLS.pack(pady=10)

eValorLS = Entry(raiz,width=40, highlightbackground="lightgreen")
eValorLS.pack(pady=5)

valorn = Label(raiz, text="Ingrese la cantidad de subintervalos(n): ", font=("Times New Roman",12), fg="white", bg="black")
valorn.pack(pady=10)

eValorn = Entry(raiz,width=40, highlightbackground="lightgreen")
eValorn.pack(pady=5)


# Etiqueta para mostrar resultados en la ventana principal
label_resultado = Label(raiz, bg="black", fg="white")
label_resultado.pack(pady=5)


#Calculos


def calcular():
    try:
        pd.options.display.float_format = '{:.10f}'.format

        funcion_usuario = eFuncion.get()
        a = float(eValorLI.get())
        b = float(eValorLS.get())
        n = int(eValorn.get())
        h = (b-a)/n
        e=(a+b)/2
        
        if a>b:
            raise ValueError("El límite superior debe ser mayor al inferior")
        elif n<0:
            raise ValueError("n debe ser positivo")

        def f(x):
            return eval(funcion_usuario)

        x = sp.symbols("x")
        f_sym = eval(funcion_usuario.replace('math.', 'sp.'))
        
        #Calculamos la segunda derivada de f(x)
        f2_sym = sp.diff(f_sym, x, 2)

        #Convertimos la derivada en una función que se puede evaluar numericamente
        f2 = sp.lambdify(x, f2_sym, 'math')
        
        #Calculamos el valor de la integral y del error
        suma = f(a) + f(b)
        for i in range(1, n):
            suma += 2 * f(a + i * h)
        
        valorMetodo = (h/2)*suma
        error= ((b-a)/(12*(n**2))) * f2(e) 
        
        total = valorMetodo - error

        respuesta = f"Valor de la integral: \n{total} \nResultado de la suma de {valorMetodo} \n- el error {error}"
            
        #Creamos la ventana de respuesta
        ventana_resultado = Toplevel(raiz)
        ventana_resultado.title("Resultado")
        ventana_resultado.geometry("400x230")
        ventana_resultado.resizable(False,False)
        
        #centrar
        ancho_ventana_resultado = 400
        alto_ventana_resultado = 230

        x2_pos = (ancho_pantalla // 2) - (ancho_ventana_resultado // 2)
        y2_pos = (alto_pantalla // 2) - (alto_ventana_resultado // 2)
        ventana_resultado.geometry(f"{ancho_ventana_resultado}x{alto_ventana_resultado}+{x2_pos}+{y2_pos}")
        
        
        frame2=Frame(ventana_resultado,bg="black",width=390, height=220) 
        frame2.place(relx=0.5, rely=0.5, anchor='center')
        
        resp = Label(ventana_resultado,text="Resultado", font=("Times New Roman",16,"bold"), bg="black", fg="lightblue")
        resp.pack(pady=20)
        
        #Determinamos que va a tener
        label_resultado_ventana = Label(ventana_resultado, text=respuesta, font=("Times New Roman", 14), bg="black", fg="white", justify="left")
        label_resultado_ventana.pack(pady=8)

        # Botón para cerrar la nueva ventana
        boton_cerrar = Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, fg="black", bg="lightblue")
        boton_cerrar.pack(pady=10)
            
    except ValueError as e:
        label_resultado.config(text=str(e))
    except Exception as e:
        label_resultado.config(text=f"Error: {str(e)}")

    
boton = Button(raiz, text="Calcular", command=calcular, bg="lightblue")
boton.pack(pady=25)



raiz.mainloop()