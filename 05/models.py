def open_file(file):
    try: 
        with open(file,"r") as file:
            file = file.read()
        return file
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {file} no pudo ser encontrado.")
    except Exception as e:
        raise Exception(f"Error al abrir el archivo: {str(e)}")



def decode(file):
    no_valido=[]
    linea = file.split("\n")
    descubre_simbolos = ("abcdefghijklmnñopqrstuvwxyzñ1234567890")
    letras = ("abcdefghijklmnñopqrstuvwxyzñ")
    numero = ("1234567890")
    
    for frase in linea:
        usuario = frase.split(",")
        id = usuario[0]
        username = usuario[1]
        email= usuario[2]
        age= usuario[3]
        location= usuario[4]

        #compruebo requisitos de id: "existe y es alfanumérica"
        if id == "":
            no_valido.append(username)
            
        
        else:
            for i in id:
                if i not in descubre_simbolos and username not in no_valido:
                    no_valido.append(username)
        
        #compruebo requisitos de username: "existe y es alfanumérico"
                    
            if username == "" and username not in no_valido:
                no_valido.append(username)
            
            else:
                for i in username:
                    i=i.lower()
                    if i not in descubre_simbolos and username not in no_valido:
                        no_valido.append(username)

        #compruebo requisitos de email: "existe y es válido (sigue el patrón user@dominio.com)"
                if email =="":
                    if username not in no_valido:
                        no_valido.append(username)
                else:
                    if "@" not in email :
                        if username not in no_valido:
                            no_valido.append(username)
                    elif ".com" not in email:
                        if username not in no_valido:
                            no_valido.append(username)

        #comrpuebo requisitos de age: "es opcional pero si aparece es un número"            
                    if age != "":
                        try:
                            int(age)
                        except:
                            if username not in no_valido:
                                no_valido.append(username)

        #compruebo requisitos de location: "es opcional pero si aparece es una cadena de texto"            
                        if location != "":
                            for i in location:
                                i = i.lower()
                                if i not in letras and username not in no_valido:
                                    no_valido.append(username)

    secret = []
    
    for usuario in no_valido:
        usuario = list(usuario)
        secret.append(usuario[0])

    resultado = ""

    for i in secret:
        
        resultado = resultado+i
       

        
        

    print(no_valido)
    print(resultado)
            


    
        
            
    

