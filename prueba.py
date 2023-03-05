from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer#para respuestas 
import random
#chat = ChatBot('Turing', preprocessors = ['chatterbot.preprocessors.clean_whitespace'])
chat = ChatBot('Turing')

#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.spanish.greetings")#speech reconnection
trainer = ListTrainer(chat)
trainer.train(['Hola','como estas','bien y tu?','Bien','¿en que puedo ayudarte?'])
trainer.train(['Buenos dias','Hola'])
trainer.train(['Buenas tardes','¿En qué puedo ayudarte?'])
trainer.train(['¿Donde puedo ubicarlos?','Barranquilla'])
trainer.train(['¿Donde estan ubicados?','Barranquilla'])
trainer.train(['¿Donde estan ubicados?','Cra 53 # 64 - 51'])
trainer.train(['¿Cual es su dirección?','Cra 53 # 64 - 51']) 
trainer.train(['¿Direccion?','Cra 53 # 64 - 51']) 
trainer.train(['¿Cual es su número telefónico?','1111111111'])
trainer.train(['¿numero telefonico?','1111111111'])
trainer.train(['¿Cual es su numero de celular','1111111111'])
trainer.train(['¿Celular','1111111111'])
trainer.train(['¿Cómo puedo contactarlos?','Buestra direccion: Cra 53 # 64 - 51 o puedes contactarnos con los numeros: 1111111111 - 2222222222'])
trainer.train(['¿Contacto?','Buestra direccion: Cra 53 # 64 - 51 o puedes contactarnos con los numeros: 1111111111 - 2222222222'])
trainer.train(['¿Cómo te llamas?','Me llamo Turing'])
trainer.train(['¿Cúal es tu nombre?','Me llamo Turing'])

while True:
    peticion = input('Tú: ')
    respuesta = chat.get_response(peticion)
    print('Turing: ', respuesta)  
