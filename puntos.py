from tkinter import *
import math
import sympy as sp
import pandas as pd

#Características básicas
raiz = Tk()
raiz.title("Calculadora WmU de Puntos")
raiz.resizable(False,False)
raiz.geometry("500x450")

#Frame para decorar
frame = Frame(raiz, bg="black",width=490, height=440) 
frame.place(relx=0.5, rely=0.5, anchor='center')

#centrar 
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()

ancho_ventana = 500
alto_ventana = 450 

x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
y_pos = (alto_pantalla // 2) - (alto_ventana // 2)
raiz.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

#Titulo
titulo = Label(raiz,text=" Calculadora - Método de Puntos", font=("Impact",20), fg="turquoise", bg="black")
titulo.pack(pady=20)

#Entradas
funcion = Label(raiz, text="Ingrese la función: ", font=("Times New Roman",12), fg="white", bg="black")
funcion.pack(pady=10)

eFuncion = Entry(raiz,width=40)
eFuncion.pack(pady=5)

valorX = Label(raiz, text="Ingrese el punto en el que se va a evaluar: ", font=("Times New Roman",12), fg="white", bg="black")
valorX.pack(pady=10)

eValorX = Entry(raiz,width=40)
eValorX.pack(pady=5)

valorn = Label(raiz, text="Ingrese el valor de n: ", font=("Times New Roman",12), fg="white", bg="black")
valorn.pack(pady=10)

opciones_n = ["Dos puntos","Tres puntos","Cinco puntos"]
metodo_Sel = StringVar()  # Variable para guardar la opción seleccionada
metodo_Sel.set(opciones_n[0])  # Valor predeterminado

# Menu desplegable para n
menu_n = OptionMenu(raiz, metodo_Sel, *opciones_n)
menu_n.config(width=10, highlightbackground="turquoise")
menu_n.pack(pady=5)

# Etiqueta para mostrar resultados en la ventana principal
label_resultado = Label(raiz, bg="black", fg="white")
label_resultado.pack(pady=5)


#Calculos


def calcular():
    try:
        pd.options.display.float_format = '{:.10f}'.format

        funcion_usuario = eFuncion.get()
        X = float(eValorX.get())
        metodo = metodo_Sel.get()
        valores_h= [0.1,0.01,0.001]
        iteraciones = []

        def f(x):
            return eval(funcion_usuario)

        x = sp.symbols("x")
        f_sym = eval(funcion_usuario.replace('math.', 'sp.'))
        
        #Calculamos las derivada de f(x)
        f2_sym = sp.diff(f_sym, x, 2)
        f3_sym = sp.diff(f_sym, x, 3)
        f5_sym = sp.diff(f_sym, x, 5)

        #Convertimos la derivada en una función que se puede evaluar numericamente
        f2 = sp.lambdify(x, f2_sym, 'math')
        f3 = sp.lambdify(x, f3_sym, 'math')
        f5 = sp.lambdify(x, f5_sym, 'math')
        
        if metodo=="Dos puntos":
            for h in valores_h:
                h_str = f"{h:.3f}" 
                valor_metodo = (f(X+h)-f(X))/h
                error = (h*f2(X))/2
                iteraciones.append([h_str, valor_metodo, round(error, 10)])
        elif metodo == "Tres puntos":
            for h in valores_h:
                h_str = f"{h:.3f}" 
                valor_metodo = (f(X+h)-f(X-h))/(2*h)
                error = ((h**2)*6)*f3(X)
                iteraciones.append([h_str, valor_metodo, round(error, 10)])
        else:
            for h in valores_h:
                h_str = f"{h:.3f}" 
                valor_metodo = (f(X-2*h)-8*f(X-h)+8*f(X+h)-f(X+2*h))/(12*h)
                error = ((h**4)*f5(X))/30
                iteraciones.append([h_str, valor_metodo, round(error, 10)])

        df = pd.DataFrame(iteraciones, columns=["h", "fórmula","error"])
        resultado_texto = df.to_string(index=False)
            
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
        
        resp = Label(ventana_resultado,text=f"Resultado {metodo}", font=("Times New Roman",16,"bold"), bg="black", fg="turquoise")
        resp.pack(pady=20)
        
        #Determinamos que va a tener
        label_resultado_ventana = Label(ventana_resultado, text=resultado_texto, font=("Times New Roman", 14), bg="black", fg="white", justify="left")
        label_resultado_ventana.pack(pady=8)

        # Botón para cerrar la nueva ventana
        boton_cerrar = Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, fg="black", bg="turquoise")
        boton_cerrar.pack(pady=10)
            
    except ValueError:
        label_resultado.config(text="Por favor, ingresa números válidos.")
    except Exception as e:
        label_resultado.config(text=f"Error: {str(e)}")

    
boton = Button(raiz, text="Calcular", command=calcular, bg="turquoise")
boton.pack(pady=25)



raiz.mainloop()