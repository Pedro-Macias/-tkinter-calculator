# importamos tkinter
from tkinter import *



def sumar():
    res.set(float(n1.get()) + float(n2.get()) )
    borrar()
def restar():
    res.set(float(n1.get()) - float(n2.get()) )
    borrar()
def producto():
    res.set(float(n1.get()) * float(n2.get()) )
    borrar()
def division():
    res.set(float(n1.get()) / float(n2.get()) )
    borrar()        

def borrar():
    n1.set('')
    n2.set('') 

# CREAR LA RAIZ
root = Tk()
root.title('calculadora')
root.resizable(True,True)
root.config(bd=30)

n1 = StringVar()
n2 = StringVar()
res = StringVar()



calculadora = Frame(root)
calculadora.pack(padx=50)


titulo= Label(calculadora,justify= 'center', text= 'CALCULADORA')
titulo.pack(anchor='n',pady=10)
titulo.config(bg='grey',fg='white',font=('Calibri',20))



numeros = Frame(calculadora)
numeros.pack()
numeros.config(width = 200 , height = 100  )


Label(numeros,justify= 'center', text= 'Numero 1',bg='lightblue',font=('Calibri',12)).pack(pady=5)
Entry(numeros,justify='center',textvariable= n1).pack(pady=5)
Label(numeros,justify= 'center', text= 'Numero 1',bg='lightblue',font=('Calibri',12)).pack(pady=5)
Entry(numeros,justify='center',textvariable=n2).pack(pady=5)

botones = Frame(calculadora)
botones.pack()
botones.config(width = 200 , height = 100 )

Button(botones, text='+', command= sumar).pack(side='left',padx=5,pady=5)
Button(botones, text='-', command= restar).pack(side='left',padx=5, pady=5)
Button(botones, text='*', command= producto).pack(side='left',padx=5, pady=5)
Button(botones, text='/', command= division).pack(side='left',padx=5, pady=5)

resultado = Frame(calculadora)
resultado.pack(pady=5)
resultado.config(width = 200 , height = 100 )


var_res = Label(resultado,justify= 'center', text= 'Resultado')
var_res.pack(pady=5)
var_res.config(bg='lightgrey',font=('Calibri',15))
Entry(resultado,justify='center',textvariable=res, state='disabled').pack(pady=5)








# INICIAR APLICACION ' siempre tiene que ir al final. 
root.mainloop()