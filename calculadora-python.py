from tkinter import*

ventana = Tk()
ventana.title("Calculadora Curso de Python By: FedeG")

ventana.configure(bg="gray")

# Estado interno
valor1         = ""
operacion      = ""
esperando_v2   = False

# Entrada de texto
e_texto = Entry(ventana, font=("calibiri 20"))
e_texto.grid(row = 0, column = 0, columnspan= 5, padx =10, pady = 15)

# Etiqueta de estado
lbl_estado = Label(ventana, text="Ingresa el valor #1 y luego selecciona una operación",
                   bg="gray", fg="yellow", font=("Calibri", 9))
lbl_estado.grid(row=6, column=0, columnspan=6, pady=(2, 8))

# Funciones
def click_boton(valor):
    e_texto.insert(END, str(valor))

def borrar():
    global valor1, operacion, esperando_v2
    e_texto.delete(0, END)
    valor1 = ""
    operacion = ""
    esperando_v2 = False
    lbl_estado.config(text="Ingresa el valor #1 y luego selecciona una operación")

# Menú de selección de operación
def seleccionar_operacion(op):
    global valor1, operacion, esperando_v2
    contenido = e_texto.get().strip()
    if contenido == "":
        lbl_estado.config(text="Ingresa el valor #1 antes de elegir la operación")
        return
    valor1 = contenido
    operacion = op
    esperando_v2 = True
    e_texto.delete(0, END)
    lbl_estado.config(text=f"Valor #1: {valor1}  |  Operación: {op}  |  Ingresa el valor #2")

# Uso de valores
def operaciones_igual():
    global valor1, operacion, esperando_v2
    if not operacion or not valor1:
        lbl_estado.config(text="Selecciona primero una operación")
        return
    valor2_str = e_texto.get().strip()
    if valor2_str == "":
        lbl_estado.config(text="Ingresa el valor #2")
        return
    try:
        v1 = float(valor1)
        v2 = float(valor2_str)
        if   operacion == "+":  resultado = v1 + v2
        elif operacion == "-":  resultado = v1 - v2
        elif operacion == "*":  resultado = v1 * v2
        elif operacion == "/":
            if v2 == 0: raise ZeroDivisionError
            resultado = v1 / v2
        elif operacion == "//":
            if v2 == 0: raise ZeroDivisionError
            resultado = int(v1) // int(v2)
        elif operacion == "^":  resultado = v1 ** v2
        elif operacion == "%":
            if v2 == 0: raise ZeroDivisionError
            resultado = v1 % v2
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        e_texto.delete(0, END)
        e_texto.insert(0, resultado)
        lbl_estado.config(text=f"{valor1} {operacion} {valor2_str} = {resultado}")
        valor1 = ""; operacion = ""; esperando_v2 = False
    except ZeroDivisionError:
        lbl_estado.config(text="Error matemático: División entre cero")
    except:
        lbl_estado.config(text="Valores no válidos")

def borrar_un_digito():
    e_texto.delete(len(e_texto.get()) - 1)


# Botones
Boton1 = Button(ventana, text="1", width=10, height=2, command= lambda: click_boton(1))
Boton2 = Button(ventana, text="2", width=10, height=2, command= lambda: click_boton(2))
Boton3 = Button(ventana, text="3", width=10, height=2, command= lambda: click_boton(3))
Boton_menos = Button(ventana, text="-", width=10, height=2, command= lambda: seleccionar_operacion("-"))

Boton4 = Button(ventana, text="4", width=10, height=2, command= lambda: click_boton(4))
Boton5 = Button(ventana, text="5", width=10, height=2, command= lambda: click_boton(5))
Boton6 = Button(ventana, text="6", width=10, height=2, command= lambda: click_boton(6))
Boton_mas = Button(ventana, text="+", width=10, height=2, command= lambda: seleccionar_operacion("+"))
Boton_div_entera = Button(ventana, text="//", width=10, height=2, command= lambda: seleccionar_operacion("//"))

Boton7 = Button(ventana, text="7", width=10, height=2, command= lambda: click_boton(7))
Boton8 = Button(ventana, text="8", width=10, height=2, command= lambda: click_boton(8))
Boton9 = Button(ventana, text="9", width=10, height=2, command= lambda: click_boton(9))
Boton_multi = Button(ventana, text="*", width=10, height=2, command= lambda: seleccionar_operacion("*"))
Boton_potencia = Button(ventana, text="^", width=10, height=2, command= lambda: seleccionar_operacion("^"))

Boton0 = Button(ventana, text="0", width=23, height=2, command= lambda: click_boton(0))
Boton_de_punto = Button(ventana, text=".", width=10, height=2, command= lambda: click_boton("."))
Boton_de_igual = Button(ventana, text="=", width=10, height=10, command= lambda: operaciones_igual())

boton_de_borrar = Button(ventana, text="AC", width=10, height=2, command= lambda: borrar())
boton_borrar_un_digito = Button(ventana, text="←", width=10, height=2, command= lambda: borrar_un_digito())
boton_de_parentesis_izquierdo = Button(ventana, text="(", width=10, height=2, command= lambda: click_boton("("))
boton_de_parentesis_derecho = Button(ventana, text=")", width=10, height=2, command= lambda: click_boton(")"))
boton_div = Button(ventana, text="/", width=10, height=2, command= lambda: seleccionar_operacion("/"))
boton_mod = Button(ventana, text="%", width=10, height=2, command= lambda: seleccionar_operacion("%"))


# Botones en pantalla
boton_de_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_borrar_un_digito.grid(row=1, column=1, padx=5, pady=5)
boton_de_parentesis_izquierdo.grid(row=1, column=2, padx=5, pady=5)
boton_de_parentesis_derecho.grid(row=1, column=3, padx=5, pady=5)
boton_div.grid(row=1, column=4, padx=5, pady=5)
boton_mod.grid(row=1, column=5, padx=5, pady=5)

Boton1.grid(row=4, column=0, padx=5, pady=5)
Boton2.grid(row=4, column=1, padx=5, pady=5)
Boton3.grid(row=4, column=2, padx=5, pady=5)
Boton_menos.grid(row=4, column=3,padx=5, pady=5)

Boton4.grid(row=3, column=0, padx=5, pady=5)
Boton5.grid(row=3, column=1, padx=5, pady=5)
Boton6.grid(row=3, column=2, padx=5, pady=5)
Boton_mas.grid(row=3, column=3, padx=5, pady=5)
Boton_de_igual.grid(row=3, rowspan=3, column=4, padx = 5, pady = 5)

Boton7.grid(row=2, column=0, padx=5, pady=5)
Boton8.grid(row=2, column=1, padx=5, pady=5)
Boton9.grid(row=2, column=2, padx=5, pady=5)
Boton_multi.grid(row=2, column=3, padx=5, pady=5)
Boton_potencia.grid(row=2, column=4, padx=5, pady=5)

Boton0.grid(row=5, column=0, columnspan=2, padx = 5, pady = 5)
Boton_de_punto.grid(row=5, column=2, padx = 5, pady = 5)
Boton_div_entera.grid(row=5, column=3, padx=5, pady=5)


ventana.mainloop()