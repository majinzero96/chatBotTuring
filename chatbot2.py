from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer#libreria con frases predeterminadas
chatbot = ChatBot('Turing: ')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish.greetings")

while True:
    peticion = input('tú: ')
    respuesta = chatbot.get_response(peticion)
    print('turing: ', respuesta)        