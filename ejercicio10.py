nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]
#alumnos= nombres.split(",")
#alumnos= list(zip(alumnos,notas_1,notas_2))

def inicisoA(nombre,nota1,nota2):
     nombre=[nom.strip() for nom in nombre.split(",")]
     alumnos={}
     for nomnb,not1,not2 in zip(nombre,nota1,nota2):
         alumnos[nomnb]=(not1,not2)
     print(alumnos)
     return alumnos



def  promedio(alumnos):
     prom=map(lambda a:(a[0]+a[1])/2,alumnos.values())
     return list(prom)

def promediototal(promedio):
     if( len(promedio) > 0):
          prom=sum( promedio)/len(promedio)
     return prom  
 
def alumnosPromedio(prom ,nombre):   
    nombre=[nom.strip() for nom in nombre.split(",")]
    alumnos={}
    for nom, nota in zip(nombre,prom):
        alumnos[nom]=(nota)
    return alumnos
def incisoD(alumnos):
     max=-1
     nom=""
     for nombre,nota in alumnos.items():
          if( nota > max):
               max=nota
               nom=nombre
     print(f" el alumno: {nom}:tiene el promedio mas alto: {max}")
def incisoE(alumnos):
     min=999
     nom=""
     for nombre,nota in alumnos.items():
          if( nota < min):
               min=nota
               nom=nombre
     print(f" el alumno: {nom}:tiene el promedio mas bajo: {min}")
# programa principal 

estructura=inicisoA(nombres,notas1,notas2)

prom=promedio(estructura)
promt=promediototal(prom)
print(promt)
alumnos=alumnosPromedio(prom,nombres)    
print(prom)
incisoD(alumnos)
incisoE(alumnos)
