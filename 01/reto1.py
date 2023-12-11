from models import *

file = open_file("./01/message_01.txt")

if file == None:
    print("Finalizando aplicación.")
else:    
    contadas = cuenta_palabra(file)
    print(contadas)


