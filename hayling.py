import os
from datetime import datetime

#test rules
hayling = {
    "0":{
    "consigna":"Su trabajo es sencillo la mayor parte del: ",
    "targets":["tiempo", "mes", "dia"],
    "relacionadas":["reloj", "calendario", "cronómetro"]
    },
    "1":{
    "consigna":"El árbitro dio por finalizado el: ",
    "targets":["partido","juego","torneo","campeonato","partida","competicion","prueba","competencia","tiempo"],
    "relacionadas":["cancha","jugador","copa","ganador","perdedor"]
    },
    "2":{
    "consigna":"En el primer renglón escriba su: ",
    "targets":["nombre","apellido","edad","domicilio","apodo","estatura","peso","firma"],
    "relacionadas":["lapiz","lapicera"]
    }, 
    "3":{
    "consigna":"El capitán quiso hundirse con su: ",
    "targets":["barco","embarcacion","nave","bote","lancha","yate"],
    "relacionadas":["auto","moto","avion","tripulación"]
    }, 
    "4":{
    "consigna":"El médico le diagnósticó una grave: ",
    "targets":["enfermedad"],
    "relacionadas":["diagnostico","muerte","salud","receta"]
    }, 
    "5":{
    "consigna":"Era una obra pensada para los: ",
    "targets":[],
    "relacionadas":[]
    }, 
    "6":{
    "consigna":"Las veredas se habían llenado de: ",
    "targets":["hojas","barro","lodo","basura","flores"],
    "relacionadas":[]
    }, 
    "7":{
    "consigna":"La mayoría de los tiburones atacan cerca de la: ",
    "targets":["orilla","costa","playa"],
    "relacionadas":["agua","arrecife","arena","rescatista","herida"]
    }, 
    "8":{
    "consigna":"El martes la ciudad se quedó sin: ",
    "targets":["luz","agua","energía","electricidad"],
    "relacionadas":["linterna","edificios","autos"]
    }, 
    "9":{
    "consigna":"Colgó el cuadro en la mejor: ",
    "targets":["pared"],
    "relacionadas":["esquina","casa","clavo","martillo","repisa"]
    }, 
    "10":{
    "consigna":"Muchos hombres se encuentran sin: ",
    "targets":["trabajo"],
    "relacionadas":["salario","dinero"]
    }, 
    "11":{
    "consigna":"El perro persiguió por toda la casa a nuestro: ",
    "targets":["gato","hermano","abuelo","tio","primo","vecino"],
    "relacionadas":["correa","dientes","colmillos"]
    }, 
    "12":{
    "consigna":"Llamó por teléfono al hermano de su: ",
    "targets":["esposo","esposa","novio","novia","pareja","amigo","amiga"],
    "relacionadas":["celular","llamada"]
    }, 
    "13":{
    "consigna":"Solo algunos pasaron el: ",
    "targets":["examen","test"],
    "relacionadas":["prueba","evaluación","clasificación"]
    }, 
    "14":{
    "consigna":"La renuncia del ministro sorprendió a todos sus: ",
    "targets":["colegas","compañeros","enemigos","jefes"],
    "relacionadas":["presidente","juez","senador","senadores"]
    }, 
}

#scoring methods
def pulir(palabra):
    palabra = palabra.strip().lower()
    return palabra

def buscar(palabra, lista):
    if palabra in lista:
        return True
    else:
        return False

def evaluar(palabra,targets,relacionadas,tiempo):
    if (t[1]-t[0])>10:
        return 2
    else:
        if buscar(palabra,targets):
            return 3
        elif buscar(palabra,relacionadas):
            return 1
        else:
            return 0

#main loop 
n=0
registro = []
while n < len(hayling):
    t=[]
    respuesta = []
    t.append(datetime.timestamp(datetime.now()))
    palabra = pulir(input(hayling[str(n)]["consigna"]))
    t.append(datetime.timestamp(datetime.now()))
    respuesta.append(palabra)
    respuesta.append(evaluar(palabra,hayling[str(n)]["targets"],hayling[str(n)]["relacionadas"],t))
    respuesta.append(t)
    registro.append(respuesta)
    print(f'Puntaje: {respuesta[1]}')
    print(f"Tiempo: {round(t[1]-t[0],2)}s")
    n = n+1
