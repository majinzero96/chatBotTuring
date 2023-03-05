import re
import random

def get_response(user_input): #definimos la entrada 
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower()) #limpiamos caractéres especiales y convertimos a minúscula
    reponse = revisarRespuestas(split_message)
    return reponse

def probabilidadMensaje(mensajeUsuario, palabrasReconocidas, respuestaSimple= False, palabrasRequeridas=[]):
    certezaMensaje = 0
    tienePalabrasRequeridas = True

    for palabras in mensajeUsuario:
        if palabras in palabrasReconocidas:
            certezaMensaje +=1

    porcentaje = float(certezaMensaje) / float (len(palabrasReconocidas))
  
    for palabras in palabrasRequeridas:
        if palabras not in mensajeUsuario:
            tienePalabrasRequeridas = False
            break 
    if tienePalabrasRequeridas or respuestaSimple:
        return int(porcentaje*100)
    else:
        return 0
    
def revisarRespuestas(message):
        probabilidadMayor ={}

        def respuesta(respuestaTuring, listaDePalabras, respuestaSimple = False, palabrasRequeridas= []):
            nonlocal probabilidadMayor
            probabilidadMayor[respuestaTuring] = probabilidadMensaje(message, listaDePalabras, respuestaSimple, palabrasRequeridas)

        respuesta('Hola Bienvenid@', ['hola'], respuestaSimple = True)
        respuesta('Buenos dias', ['buenos'], respuestaSimple = True)
        respuesta('Buenas tardes', ['buenas'], respuestaSimple = True)
        #respuesta('Estoy bien y tu?', ['como','estas','te','vas','tal','bien'], palabrasRequeridas = ['como'])
        respuesta('Estoy bien y tu?', ['como','estas','te','vas','sientes','todo','bien'], respuestaSimple= True)
        respuesta('Cra 53 # 64 - 51 Barranquilla, Colombia', ['donde','estan','ubicados','ubicacion','encontrarlos','encontrar','direccion'],respuestaSimple = True)
        respuesta('Nuestro horario de atención es de 8 am a 12 pm y de 2 pm a 6 pm', ['horario','atienden','atender','hora'],respuestaSimple=True)
        respuesta('De nada', ['muchas','gracias','agradezco','ty'], respuestaSimple=True)

        best_match = max(probabilidadMayor, key=probabilidadMayor.get)        
        #print(probabilidadMayor)

        return palDesconocida() if probabilidadMayor[best_match] < 1 else best_match
        

def palDesconocida():
    #response =['No puedo ayudarte, en que otra cosa puedo ayudarte?']
    response =['No puedo ayudarte, en que otra cosa puedo ayudarte?','No te entiendo','escribe otra cosa']#[random.randrange(3)]
    return random.choice(response)
    

while True:
   print("Turing : "+ get_response(input('TU: ')))