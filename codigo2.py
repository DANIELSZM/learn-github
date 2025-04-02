nombre = "daniel stiven"
apellido =  "zambrano mora" #apellido completo

def saludo (nombre, apellido):
    print("hola soy " + nombre +  " " + apellido)
    
def saludar_bien (nombre_completo):
    print(f'hola soy {nombre_completo}, ¿como estas?')
    
print("funcion saludar bien:  ")
saludar_bien("daniel zambrano") 

print("\nfuncion saludo:  ")
saludo("daniel", "zambrano") # llamar funcion saludo y saludar bien para ver la diferencia