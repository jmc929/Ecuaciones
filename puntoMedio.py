from tkinter import *
import math
import sympy as sp
import pandas as pd

#Características básicas
raiz = Tk()
raiz.title("Calculadora WmU Punto Medio")
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
titulo = Label(raiz,text=" Calculadora - Método del Punto Medio", font=("Impact",20), fg="silver", bg="black")
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

valorn = Label(raiz, text="Elija el valor de n: ", font=("Times New Roman",12), fg="white", bg="black")
valorn.pack(pady=10)

opciones_n = [0, 1, 2, 3]
n_seleccionado = IntVar()  # Variable para guardar la opción seleccionada
n_seleccionado.set(opciones_n[0])  # Valor predeterminado

# Menu desplegable para n
menu_n = OptionMenu(raiz, n_seleccionado, *opciones_n)
menu_n.config(width=10, highlightbackground="silver")
menu_n.pack(pady=5)

# Etiqueta para mostrar resultados en la ventana principal
label_resultado = Label(raiz, bg="black", fg="white")
label_resultado.pack(pady=5)


#Calculos


def calcular():
    try:
        pd.options.display.float_format = '{:.10f}'.format

        funcion_usuario = eFuncion.get()
        x1 = float(eValorLI.get())
        x2 = float(eValorLS.get())
        n = n_seleccionado.get()
        e = (x2+x1)/2
        
        if x1 >= x2:
            raise ValueError("El límite inferior debe ser menor que el límite superior.")

        def f(x):
            return eval(funcion_usuario)

        x = sp.symbols("x")
        f_sym = eval(funcion_usuario.replace('math.', 'sp.'))
        
        #Calculamos las derivada de f(x)
        f2_sym = sp.diff(f_sym, x, 2)
        f3_sym = sp.diff(f_sym, x, 3)
        f4_sym = sp.diff(f_sym, x, 4)

        #Convertimos la derivada en una función que se puede evaluar numericamente
        f2 = sp.lambdify(x, f2_sym, 'math')
        f3 = sp.lambdify(x, f3_sym, 'math')
        f4 = sp.lambdify(x, f4_sym, 'math')
        
        if n==0:
            h = x2-x1
            x0 = x1 + h/2
            resultado = h*f(x0)+ ((h**3/24)*f2(e))
        elif n==1:
            h = x2-x1
            resultado = (3*h/2)*(f(x1)+f(x2)) + ((3*(h**3)/4)*f2(e))
        elif n==2:
            h = (x2-x1)/2
            resultado = (4*h/3)*(2*f(x1)-f((x2+x1)/2)+2*f(x2)) + ((14/(h**5)*45)*f2(e))
        else:
            h = (x2-x1)/3
            resultado = (5*h/24)*(11*f(x1)+f(x1+h)+f(x1+2*h)+11*f(x2)) + ((95/(h**5)*144)*f4(e))


        respuesta = f"Valor de la integral: \n{resultado}"
            
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
        
        resp = Label(ventana_resultado,text="Resultado", font=("Times New Roman",16,"bold"), bg="black", fg="silver")
        resp.pack(pady=20)
        
        #Determinamos que va a tener
        label_resultado_ventana = Label(ventana_resultado, text=respuesta, font=("Times New Roman", 14), bg="black", fg="white", justify="left")
        label_resultado_ventana.pack(pady=8)

        # Botón para cerrar la nueva ventana
        boton_cerrar = Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, fg="black", bg="silver")
        boton_cerrar.pack(pady=10)
            
    except ValueError as e:
        label_resultado.config(text=str(e))
    except Exception as e:
        label_resultado.config(text=f"Error: {str(e)}")

    
boton = Button(raiz, text="Calcular", command=calcular, bg="silver")
boton.pack(pady=25)



raiz.mainloop()