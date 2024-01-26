def open_file(file):
    try:
        with open(file, "r") as file:
            file = file.read()
        
        return file
    
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{file}' no pudo ser encontrado.")
    except Exception as e:
        raise Exception(f"Error al abrir el archivo: {str(e)}")
    
    
    

def decode(file):
    archivos_reales=[]
    for linea in file.split("\n"):
        #linea=linea.lower()

        alfa_chain, checksum = linea.split("-")
        symbol_dic = {}
        contador = 0
        for symbol in alfa_chain:
            if symbol in symbol_dic:
                if symbol_dic[symbol] ==1:
                    contador += 1
                symbol_dic[symbol] +=1
            else:
                symbol_dic[symbol]=1
        
        alfa_ok_list = []
        for clave, valor in symbol_dic.items():
            if valor == 1:
                alfa_ok_list.append(clave)
        alfa_ok= ""
        for i in alfa_ok_list:   
            alfa_ok = alfa_ok+i     
        
        if str(alfa_ok)== str(checksum):
            archivos_reales.append(checksum)
           
        else:
            continue 
        
    print(archivos_reales[32])     
       
    


                  

            

        
        



