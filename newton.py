from tkinter import *
import math
import sympy as sp
import pandas as pd

#Características básicas
raiz = Tk()
raiz.title("Calculadora WmU Newton")
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
titulo = Label(raiz,text=" Calculadora - Método de Newton", font=("Impact",20), fg="#FFDAB9", bg="black")
titulo.pack(pady=20)

#Entradas
funcion = Label(raiz, text="Ingrese la función: ", font=("Times New Roman",12), fg="white", bg="black")
funcion.pack(pady=10)

eFuncion = Entry(raiz,width=40, highlightbackground="#FFDAB9")
eFuncion.pack(pady=5)

valorp0= Label(raiz, text="Ingrese el valor de p0: ", font=("Times New Roman",12), fg="white", bg="black")
valorp0.pack(pady=10)

eValorp0 = Entry(raiz,width=40, highlightbackground="#FFDAB9")
eValorp0.pack(pady=5)

valorTol = Label(raiz, text="Ingrese el valor de la tolerancia: ", font=("Times New Roman",12), fg="white", bg="black")
valorTol.pack(pady=10)

eValorTol = Entry(raiz,width=40, highlightbackground="#FFDAB9")
eValorTol.pack(pady=5)

valorn = Label(raiz, text="Ingrese el número máximo de iteraciones: ", font=("Times New Roman",12), fg="white", bg="black")
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
        p0 = float(eValorp0.get())
        tol= float(eValorTol.get())
        n = int(eValorn.get())
        i = 1
        
        if tol<0 or n<0:
            raise ValueError("Recuerde que la tolerancia y el número de iteraciones son números positivos")

        def f(x):
            return eval(funcion_usuario)
        
        x = sp.symbols("x")
        f_sym = eval(funcion_usuario.replace('math.', 'sp.'))
        
        f1_sym = sp.diff(f_sym, x, 1)

        #Convertimos la derivada en una función que se puede evaluar numericamente
        f1 = sp.lambdify(x, f1_sym, 'math')

        iteraciones = []
        while i<=n:
            pi = p0 - (f(p0)/f1(p0))
            
            resta = abs(pi - p0)
            
            iteraciones.append([i,pi,round(resta,10)])
            
            if resta<tol:
                respuesta = f"La respuesta final es: \n{pi}\nY la tabla de iteraciones es:"
                break
            
            i+=1
            p0=pi
            
            respuesta = "No se pudo resolver con esas iteraciones \nLa tabla de iteraciones es:"


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
        
        resp = Label(ventana_resultado,text="Respuesta", font=("Times New Roman",12,"bold"), bg="black", fg="#FFDAB9")
        resp.pack(pady=20)
        
        label_respuesta_ventana = Label(ventana_resultado, text=respuesta, font=("Times New Roman", 13), bg="black", fg="white", justify="left")
        label_respuesta_ventana.pack(pady=8)
        
        label_resultado_ventana = Label(ventana_resultado, text=resultado_texto, font=("Times New Roman", 12), bg="black", fg="white", justify="left")
        label_resultado_ventana.pack(pady=10)
        
        # Botón para cerrar la nueva ventana
        boton_cerrar = Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy, fg="black", bg="#FFDAB9")
        boton_cerrar.pack(pady=15)
            
    except ValueError as e:
        label_resultado.config(text=str(e))
    except Exception as e:
        label_resultado.config(text=f"Error: {str(e)}")

    
boton = Button(raiz, text="Calcular", command=calcular, bg="#FFDAB9")
boton.pack(pady=25)



raiz.mainloop()