from tkinter import *
import math
import sympy as sp
import pandas as pd

#Características básicas
raiz = Tk()
raiz.title("Calculadora WmU Secante")
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
titulo = Label(raiz,text=" Calculadora - Método de la Secante", font=("Impact",20), fg="aquamarine", bg="black")
titulo.pack(pady=20)

#Entradas
funcion = Label(raiz, text="Ingrese la función: ", font=("Times New Roman",12), fg="white", bg="black")
funcion.pack(pady=10)

eFuncion = Entry(raiz,width=40, highlightbackground="aquamarine")
eFuncion.pack(pady=5)

valorx0 = Label(raiz, text="Ingrese el valor de x0: ", font=("Times New Roman",12), fg="white", bg="black")
valorx0.pack(pady=10)

eValorx0 = Entry(raiz,width=40, highlightbackground="aquamarine")
eValorx0.pack(pady=5)

valorx1 = Label(raiz, text="Ingrese el valor de x1: ", font=("Times New Roman",12), fg="white", bg="black")
valorx1.pack(pady=10)

eValorx1 = Entry(raiz,width=40, highlightbackground="aquamarine")
eValorx1.pack(pady=5)

valorn = Label(raiz, text="Ingrese la cantidad máxima de iteraciones: ", font=("Times New Roman",12), fg="white", bg="black")
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
        x0 = float(eValorx0.get())
        x1 = float(eValorx1.get())
        n = int(eValorn.get())
        
        if n<0:
            raise ValueError("El número de intervalos debe ser positivo")

        def f(x):
            return eval(funcion_usuario)

        x = sp.symbols("x")
        f_sym = eval(funcion_usuario.replace('math.', 'sp.'))
        
        iteraciones = []

        for k in range (1, n + 1):
            f_x0 = f(x0)
            f_x1 = f(x1)
            
            x2 = (x0 * f_x1 - x1 * f_x0) / (f_x1 - f_x0)

            otro = abs(x1 - x0)

            # Guardamos los resultados de la iteración actual en una lista
            iteraciones.append([k, x0, round(otro, 10)])
            
            # Actualizamos los valores de x0 y x1 para la siguiente iteración
            x0 = x1
            x1 = x2
            
            print(abs(x0-x1))
            if abs(x1-x0)<abs(0.0001):
                respuesta = f"El método funcionó, la respuesta es: \n{x1}\n La tabla de iteraciones es: "
            else:
                respuesta = "El método no es adecuado para el problema,\n La tabla de iteraciones es:"
            
        df = pd.DataFrame(iteraciones, columns=["Iteración", "p","p-pn"])
        resultado_texto = df.to_string(index=False)
            
        #Creamos la ventana de respuesta
        ventana_resultado = Toplevel(raiz)
        ventana_resultado.title("Resultados de Iteraciones")
        ventana_resultado.geometry("350x350")
        ventana_resultado.resizable(False,True)
        
        #centrar
        ancho_ventana_resultado = 350
        alto_ventana_resultado = 350

        x2_pos = (ancho_pantalla // 2) - (ancho_ventana_resultado // 2)
        y2_pos = (alto_pantalla // 2) - (alto_ventana_resultado // 2)
        ventana_resultado.geometry(f"{ancho_ventana_resultado}x{alto_ventana_resultado}+{x2_pos}+{y2_pos}")
        
        
        frame2=Frame(ventana_resultado,bg="black",width=340, height=340) 
        frame2.place(relx=0.5, rely=0.5, anchor='center')
        
        resp = Label(ventana_resultado,text=respuesta, font=("Times New Roman",12,"bold"), bg="black", fg="white")
        resp.pack(pady=25)
        
        #Determinamos que va a tener
        label_resultado_ventana = Label(ventana_resultado, text=resultado_texto, font=("Times New Roman", 12), bg="black", fg="white", justify="left")
        label_resultado_ventana.pack(pady=10)

        # Botón para cerrar la nueva ventana
        boton_cerrar = Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, fg="black", bg="aquamarine")
        boton_cerrar.pack(pady=10)
            
    except ValueError as e:
        label_resultado.config(text=str(e))
    except Exception as e:
        label_resultado.config(text=f"Error: {str(e)}")

    
boton = Button(raiz, text="Calcular", command=calcular, bg="aquamarine")
boton.pack(pady=25)



raiz.mainloop()