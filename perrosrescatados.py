
# Perros Rescatados

print("Bienvenido/a a nuestro programa de Perros rescatados")

class Perros():
    def __init__(self, nombreR, edadR, pesoR, razaR, vacunaR):
        self.nombre = nombreR
        self.edad = edadR
        self.peso = pesoR
        self.raza = razaR
        self.vacunacion = vacunaR

    def anioVacunacion(self, anioActual=2020):
        if (self.vacunacion):
            return anioActual - self.vacunacion
        else:
            print("No está registrada la última fecha de vacunación")

    def mostrarPerro(self):
        print("Se encunetra registrado " + self.nombre + " que tiene " + str(self.edad) + " años, actualmente pesa " + str(self.peso) + " su raza es " + self.raza + " y la última vacunación fue en " + str(self.vacunacion))       
 
respuesta = input("¿Quieres agregar un perro rescatado? S(si) N(no)\n ").upper()

while respuesta == "S":
    print("Muy bien, vamos a darle la Bienvenida a una nueva mascota")
    nombreMascota = input("Ingresa el nombre del nuevo perro \n")
    edadMascota = int(input("Ingresa la edad \n"))
    pesoMascota = int(input("Ingresa el peso del nuevo perro \n"))
    razaMascota = input("Ingresa la raza \n")
    ultimaVacunacion = int(input("Ingresa el año de su última vacunación \n"))
    mascotaNueva = Perros(nombreR=nombreMascota, edadR=edadMascota, pesoR=pesoMascota, razaR=razaMascota, vacunaR=ultimaVacunacion)
    
    print("Gracias, hemos registrado a " + mascotaNueva.nombre + " de " + str(mascotaNueva.edad) + " años, que pesa " + str(mascotaNueva.peso) + " kg. y Su raza es " + mascotaNueva.raza + ". La fecha de su última vacunación fue en el año " + str(mascotaNueva.vacunacion)) 
    
    datoVacunacion = mascotaNueva.anioVacunacion(anioActual=2020)
    print("La última vacunación fue hace " + str(datoVacunacion) + " años ")
    if (datoVacunacion <= 2):
        print("Las vacunas están al día")
    else:
        print("Debe aplicarse nuevas dosis de vacunas")    

    respuesta = input("¿Quieres agregar un perro rescatado? S(si) N(no)\n ").upper()

print("Muchas gracias, has finalizado. Nos vemos pronto para rescatar más perritos")



# Base de datos. Perros ya registrados en el refugio de mascotas

can1 = Perros(nombreR="Shina", edadR=2, pesoR=7, razaR="Salchicha", vacunaR=2019) 
can2 = Perros(nombreR="Paul", edadR=1, pesoR=10, razaR="Ovejero", vacunaR=2019)  
can3 = Perros(nombreR="Copito", edadR=3, pesoR=4, razaR="Caniche", vacunaR=2018)  
can4 = Perros(nombreR="Panchita", edadR=6, pesoR=7, razaR="Cocker", vacunaR=2016) 
can5 = Perros(nombreR="Gala", edadR=4, pesoR=8, razaR="Cruza", vacunaR=2017)  

listaMascotas =[]
listaMascotas.append(can1)
listaMascotas.append(can2)
listaMascotas.append(can3)
listaMascotas.append(can4)
listaMascotas.append(can5)
       

consultarDato = input("¿Desea consultar los datos de algún can? S(si) N(no) \n").upper()
if consultarDato == "S":    
    numeroPerro = int(input("Ingresá el número del perro \n"))
    listaMascotas[numeroPerro-1].mostrarPerro()   
else:
    print("Muchas gracias, nos veremos en otra ocasión")  

print("Gracias, te esperamos para un nuevo ingreso")
input("Si ya no deseas realizar ninguna tarea más, toca ENTER para salir")




    



  



