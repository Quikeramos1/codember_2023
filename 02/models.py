import re

def open_file(file):
    try:
        open_file = open(file, "r")
        return open_file 

    except:
        return print("El archivo no ha podido ser abierto")

        
def deshide(open_file):
   linea = open_file.read()
   solucion = []
   contador = 0
   for i in linea:
       if i == "#":
           contador +=1
       elif i == "@":
           contador -=1
       elif i == "*":
           contador = contador * contador
       elif i == "&":
           solucion.append(contador)
   solucion = formato(solucion)
   
   return solucion          
       
def formato(solucion):
    solucion = str(solucion)
    solucion = solucion.strip("[]")
    solucion = re.sub(",","",solucion)
    solucion = re.sub(" ","",solucion)
    return solucion


