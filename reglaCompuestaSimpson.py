from tkinter import *
import math
import sympy as sp
import pandas as pd

#Características básicas
raiz = Tk()
raiz.title("Calculadora WmU Regla Compuesta Simpson")
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
titulo = Label(raiz,text="Método de la Regla Compuesta Simpson", font=("Impact",20), fg="cadetblue", bg="black")
titulo.pack(pady=20)

#Entradas
funcion = Label(raiz, text="Ingrese la función: ", font=("Times New Roman",12), fg="white", bg="black")
funcion.pack(pady=10)

eFuncion = Entry(raiz,width=40, highlightbackground="cadetblue")
eFuncion.pack(pady=5)

valorLS = Label(raiz, text="Ingrese el valor del límite superior: ", font=("Times New Roman",12), fg="white", bg="black")
valorLS.pack(pady=10)

eValorLS = Entry(raiz,width=40, highlightbackground="cadetblue")
eValorLS.pack(pady=5)

valorLI = Label(raiz, text="Ingrese el valor del límite inferior: ", font=("Times New Roman",12), fg="white", bg="black")
valorLI.pack(pady=10)

eValorLI = Entry(raiz,width=40, highlightbackground="cadetblue")
eValorLI.pack(pady=5)

valorn = Label(raiz, text="Ingrese el valor de n: ", font=("Times New Roman",12), fg="white", bg="black")
valorn.pack(pady=10)

eValorn = Entry(raiz,width=40)
eValorn.pack(pady=5)

# Etiqueta para mostrar resultados en la ventana principal
label_resultado = Label(raiz, bg="black", fg="white")
label_resultado.pack(pady=5)


#Calculos



def calcular():
    try:
        pd.options.display.float_format = '{:.10f}'.format

        funcion_usuario = eFuncion.get()
        b = float(eValorLS.get())
        a = float(eValorLI.get())
        n = int(eValorn.get())
        h = (b-a)/n
        sumaK = 0
        sumaW = 0
        
        if n <= 0:
            raise ValueError("El valor de n debe ser un número entero positivo.")
        elif n % 2 != 0:
            raise ValueError("n debe ser un número par")
        elif a>b:
            raise ValueError("El límite superior debe ser mayor al inferior")

        def f(x):
            return eval(funcion_usuario)

        x = sp.symbols("x")
        f_sym = eval(funcion_usuario.replace('math.', 'sp.'))
        
        f4_sym = sp.diff(f_sym, x, 4)

        #Convertimos la derivada en una función que se puede evaluar numericamente
        f4 = sp.lambdify(x, f4_sym, 'math')
        
        for j in range(1, n//2):
            x2j = a + 2*j*h
            fx2j = f(x2j)
            sumaK += fx2j
            
        print(sumaK)
            
        for j in range (1, n//2 + 1):
            x2j = a + (2*j-1)*h
            fx2j = f(x2j)
            sumaW += fx2j
        
        print(sumaW)

        v_metodo = (h/3)*(f(a)+2*sumaK+4*sumaW+f(b))
        error = (((b-a)/180)*h**4*f4((a+b)/2))
        
        resultado = v_metodo - error 
            
        respuesta = f"El valor de la integral es: \n{resultado}\nresultado de {v_metodo}-\nel error= {error} "
            
        respuesta = f"El valor de la integral es \n{resultado}"
            
        #Creamos la ventana de respuesta
        ventana_resultado = Toplevel(raiz)
        ventana_resultado.title("Resultados de Iteraciones")
        ventana_resultado.geometry("350x250")
        ventana_resultado.resizable(False,True)
        
        #centrar
        ancho_ventana_resultado = 350
        alto_ventana_resultado = 250

        x2_pos = (ancho_pantalla // 2) - (ancho_ventana_resultado // 2)
        y2_pos = (alto_pantalla // 2) - (alto_ventana_resultado // 2)
        ventana_resultado.geometry(f"{ancho_ventana_resultado}x{alto_ventana_resultado}+{x2_pos}+{y2_pos}")
        
        
        frame2=Frame(ventana_resultado,bg="black",width=340, height=240) 
        frame2.place(relx=0.5, rely=0.5, anchor='center')
        
        resp = Label(ventana_resultado,text="Respuesta", font=("Times New Roman",12,"bold"), bg="black", fg="cadetblue")
        resp.pack(pady=25)
        
        #Determinamos que va a tener
        label_resultado_ventana = Label(ventana_resultado, text=respuesta, font=("Times New Roman", 12), bg="black", fg="white", justify="left")
        label_resultado_ventana.pack(pady=10)

        # Botón para cerrar la nueva ventana
        boton_cerrar = Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, fg="black", bg="cadetblue")
        boton_cerrar.pack(pady=10)
            
    except ValueError as e:
        label_resultado.config(text=str(e))
    except Exception as e:
        label_resultado.config(text=f"Error: {str(e)}")

    
boton = Button(raiz, text="Calcular", command=calcular, bg="cadetblue")
boton.pack(pady=25)



raiz.mainloop()