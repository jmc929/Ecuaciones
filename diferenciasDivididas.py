from tkinter import *
import math
import sympy as sp
import pandas as pd

#Características básicas
raiz = Tk()
raiz.title("Calculadora WmU Diferencias Divididas")
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
titulo = Label(raiz,text="Método de las Diferencias Divididas", font=("Impact",20), fg="cornflowerblue", bg="black")
titulo.pack(pady=20)

#Entradas
funcion = Label(raiz, text="Ingrese la función: ", font=("Times New Roman",12), fg="white", bg="black")
funcion.pack(pady=10)

eFuncion = Entry(raiz,width=40, highlightbackground="cornflowerblue")
eFuncion.pack(pady=5)

valorxi = Label(raiz, text="Ingrese el valor inicial de xi: ", font=("Times New Roman",12), fg="white", bg="black")
valorxi.pack(pady=10)

eValorxi = Entry(raiz,width=40, highlightbackground="cornflowerblue")
eValorxi.pack(pady=5)


valorAxi = Label(raiz, text="Ingrese en qué cantidad aumenta xi: ", font=("Times New Roman",12), fg="white", bg="black")
valorAxi.pack(pady=10)

eValorAxi = Entry(raiz,width=40, highlightbackground="cornflowerblue")
eValorAxi.pack(pady=5)

# Etiqueta para mostrar resultados en la ventana principal
label_resultado = Label(raiz, bg="black", fg="white")
label_resultado.pack(pady=5)


#Calculos



def calcular():
    try:
        pd.options.display.float_format = '{:.10f}'.format

        funcion_usuario = eFuncion.get()
        xi = (float(eValorxi.get()))
        aumento = float(eValorAxi.get())
        
        if aumento<0:
            raise ValueError("Recuerde que el aumento debe ser positivo")

        def f(x):
            return eval(funcion_usuario)
        
        iteraciones = []

        for i in range (0, 5):
            if i==0:
                f0 = f(xi)
                iteraciones.append([i,xi,f0,0,0,0,0])
            elif i == 1:
                x1 = round(xi + aumento,1)
                f1 = f(x1)
                f21 = (f1-f0)/(x1-xi)
                iteraciones.append([i,x1,f1,f21,round(0,0),0,0])
            elif i == 2:
                x2 = xi + 2 * aumento
                f2 = f(x2)
                f22 = (f2-f1)/(x2-x1)
                f32 = (f22-f21)/(x2-xi)
                iteraciones.append([i,x2,f2,f22,f32,0,0])
            elif i == 3:
                x3 = xi + 3 * aumento
                f3 = f(x3)
                f23 = (f3-f2)/(x3-x2)
                f33 = (f23-f22)/(x3-x1) 
                f43 = (f33-f32)/(x3-xi)
                iteraciones.append([i,x3,f3,f23,f33,f43,0])
            else:
                x4 = xi + 4 * aumento
                f4 = f(x4)
                f24 = (f4-f3)/(x4-x3)
                f34 = (f24-f23)/(x4-x2)
                f44 = (f34-f33)/(x4-x1)
                f54 = (f44-f43)/(x4-xi)
                iteraciones.append([i,x4,f4,f24,f34,f44,f54])
                coeficientes = [f0,f21,f32,f43,f54]
            
 
        respuesta = f"Los coeficientes del polinomio de lagrange son: \n{coeficientes}\nLa tabla de iteraciones es: "

            
        df = pd.DataFrame(iteraciones, columns=["i", "xi", "f(xi)", "   f(xi+xi+1)", "f(xi,xi+1,xi+2)", "f(xi,xi+1,xi+2,xi+3)", "f(xi,xi+1,xi+2,xi+3,xi+4)"])
        resultado_texto = df.to_string(index=False)
            
        #Creamos la ventana de respuesta
        ventana_resultado = Toplevel(raiz)
        ventana_resultado.title("Resultados de Iteraciones")
        ventana_resultado.geometry("800x350")
        ventana_resultado.resizable(False,True)
        
        #centrar
        ancho_ventana_resultado = 800
        alto_ventana_resultado = 350

        x2_pos = (ancho_pantalla // 2) - (ancho_ventana_resultado // 2)
        y2_pos = (alto_pantalla // 2) - (alto_ventana_resultado // 2)
        ventana_resultado.geometry(f"{ancho_ventana_resultado}x{alto_ventana_resultado}+{x2_pos}+{y2_pos}")
        
        
        frame2=Frame(ventana_resultado,bg="black",width=790, height=340) 
        frame2.place(relx=0.5, rely=0.5, anchor='center')
        
        resp = Label(ventana_resultado,text=respuesta, font=("Times New Roman",12,"bold"), bg="black", fg="white")
        resp.pack(pady=25)
        
        #Determinamos que va a tener
        label_resultado_ventana = Label(ventana_resultado, text=resultado_texto, font=("Times New Roman", 12), bg="black", fg="white", justify="left")
        label_resultado_ventana.pack(pady=10)

        # Botón para cerrar la nueva ventana
        boton_cerrar = Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, fg="black", bg="cornflowerblue")
        boton_cerrar.pack(pady=10)
            
    except ValueError as e:
        label_resultado.config(text=str(e))
    except Exception as e:
        label_resultado.config(text=f"Error: {str(e)}")

    
boton = Button(raiz, text="Calcular", command=calcular, bg="cornflowerblue")
boton.pack(pady=25)



raiz.mainloop()