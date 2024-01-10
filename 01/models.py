
def open_file(file):
    
    try:
        open_file = open(file, "r")
        return open_file 

    except:
        return print("El archivo no ha podido ser abierto")


     



def cuenta_palabra(file):
    if file == None:
        print("")
    else:
        contadas = {}
        
        for letra in file:
            lista = "".join(letra.lower())
            lista = lista.split()
        for letra in lista:
            if letra not in contadas:
                contadas[letra] = 1
            else:
                contadas[letra] +=1
                
        contadas = str(contadas)
        simbols="{}[]:',"""
        lcontadas="".join(i for i in contadas if i not in simbols)
        llcontadas = lcontadas.replace(' ','')

    return llcontadas
    