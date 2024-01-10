def open_file(file):

    try:
        with open(file, "r") as file:
            file = file.read()
        
        return file
    
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{file}' no pudo ser encontrado.")
    except Exception as e:
        raise Exception(f"Error al abrir el archivo: {str(e)}")


def valid_pass(file):
    invalid_pass = []
    valid_pass = []
    

    for linea in file.split("\n"):
        
        pol_pass,password = linea.split(":")
        nums,letter = pol_pass.split(" ")
        mini,maxi = nums.split("-")
        
        if letter not in password:
            invalid_pass.append(password)
        else:
            contado = password.count(letter)
            if  int(contado) < int(mini) or int(contado) > int(maxi):
                invalid_pass.append(password)
                     
            else:
                valid_pass.append(password)
                
        
            
            
    return invalid_pass[41]


