#Librerias
import pandas as pd
import menu as m 
import acciones as a

#Cargar archivos excel

excel1= "1.xlsx"
dfp=pd.read_excel(excel1)

excel2="libros.xlsx"
dfl=pd.read_excel(excel2)

#MENU
options=True
buscar=0



while(options==True):
    buscar = m.mostrarMenu()
    if(buscar == "a"):
        a.listaPersonas(dfp)
    elif(buscar == "b"):
        a.ordenarPersonas(dfp)
    elif(buscar=="c"):
        a.registroPersonas()    
    elif(buscar == "d"):
        a.listaLibros(dfl)
    elif(buscar=="e"):
        a.buscarLibros() 
    elif(buscar=="f"):
        a.prestarLibros()       
    elif(buscar == "g"):
        a.verPrestamo() 
    elif(buscar=="s"):
        options=False

      
        










